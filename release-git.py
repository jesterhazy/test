#!/usr/bin/env python3

import argparse
import json
import logging
import os
import re
import sys

import boto3

OAUTH_SECRET_ID = '/codebuild/github/oauth'

logging.basicConfig(level=logging.INFO)
logging.getLogger('boto3').setLevel(logging.ERROR)
logging.getLogger('botocore').setLevel(logging.ERROR)
logger = logging.getLogger()


class Version(object):
    # a subset of PEP 440
    _regex = re.compile(r'''
        ^\s*
        v?
        (?P<major>\d+)
        (?:\.(?P<minor>\d+))?
        (?:\.(?P<patch>\d+))?
        (?:\.(?P<pre>(?P<pre_label>a|b|rc)(?P<pre_n>\d+)))?
        (?:\.post(?P<post>\d+))?
        (?:\.dev(?P<dev>\d+))?
        \s*$
    ''', re.VERBOSE | re.IGNORECASE)

    def __init__(self, major, minor=0, patch=0, pre=None, post=None, dev=None):
        self.major = major
        self.minor = minor
        self.patch = patch
        self.pre = pre
        self.post = post
        self.dev = dev

        if len([x for x in [pre, post, dev] if x is not None]) > 1:
            raise ValueError(f'invalid version: {str(self)}')

    @staticmethod
    def parse(version):
        match = Version._regex.search(version)
        if not match:
            raise ValueError(f'invalid version: {version_string}')

        return Version(
                int(match.group('major') or 0),
                int(match.group('minor') or 0),
                int(match.group('patch') or 0),
                (match.group('pre_label'), int(match.group('pre_n'))) if match.group('pre') else None,
                int(match.group('post')) if match.group('post') else None,
                int(match.group('dev')) if match.group('dev') else None
            )

    def __str__(self):
        parts = [str(x) for x in [self.major, self.minor, self.patch]]

        if self.pre:
            parts.append(f'{self.pre[0]}{self.pre[1]}')

        if self.post is not None:
            parts.append(f'post{self.post}')

        if self.dev is not None:
            parts.append(f'dev{self.dev}')

        return '.'.join(parts).lower()

    def increment(self, segment):
        incr = None
        if segment == 'major':
            incr = Version(self.major + 1)
        elif segment == 'minor':
            incr = Version(self.major, self.minor + 1)
        elif segment == 'patch':
            incr = Version(self.major, self.minor, self.patch + 1)
        elif segment == 'pre':
            if self.pre:
                pre = (self.pre[0], self.pre[1] + 1)
                patch = self.patch
            elif self.dev:
                pre = ('a', 0)
                patch = self.patch
            else:
                pre = ('a', 0)
                patch = self.patch + 1
            incr = Version(self.major, self.minor, patch, pre=pre)
        elif segment == 'post':
            if self.pre or self.dev:
                raise ValueError(f'can\'t increment post on a prerelease version: {str(self)}')
            post = self.post + 1 if self.post else 0
            incr = Version(self.major, self.minor, self.patch, post=post)
        elif segment == 'dev':
            if self.pre:
                raise ValueError(f'can\'t increment dev on a prerelease version: {str(self)}')
            if self.dev:
                dev = self.dev + 1
                patch = self.patch
            else:
                dev = 0
                patch = self.patch + 1
            incr = Version(self.major, self.minor, patch, dev=dev)

        return incr


def get_oauth_token():
    secrets_client = boto3.client('secretsmanager')
    return secrets_client.get_secret_value(SecretId=OAUTH_SECRET_ID)['SecretString']


def current_version(min_version):
    # TODO - get from git, then parse with version, compare with min_version...
    pass


def next_version(current_version, segment):
    v1 = Version(current_version)
    v2 = v1.increment(segment)
    return v2


def parse_args(args):
    parser = argparse.ArgumentParser(os.path.basename(__file__))
    parser.set_defaults(func=lambda x: parser.print_usage())
    parser.add_argument('--prepare', help='prepare a release', action='store_true')
    parser.add_argument('--publish', help='publish a release', action='store_true')
    parser.add_argument('--min-version', help='set the minimum release number',
        default='0.1.0', type=str)

    parsed = parser.parse_args(args)
    if not (parsed.prepare or parsed.publish):
        parser.error('--prepare or --publish required')


def main(args):
    args = parse_args(args)
    oauth_token = get_oauth_token()

    # ok, so we can do stuff with versions!
    print(Version.parse('1.0.4.a1').increment('post'))


    # need to
    # - get version from git
    # - update the version file - useless move in TFS, but single-source file for python projects
    # - update the change log
    # - commit and tag the changes (local)

    # then for publish
    # push local commits and tags
    # create a GH release on the tag, with the new changelog stuff in the release notes
    # really ought to have some tests for this shit!

    # then fix for codepipeline



if __name__ == '__main__':
    main(sys.argv[1:])
