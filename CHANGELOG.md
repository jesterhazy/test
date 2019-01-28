# Changelog

## 2.0.0

### Breaking changes

 * Reducing test flakiness
 * Bumping up version to 1.18.0 for horovod release

### New features

 * Add 'tuner' to imports in 'sagemaker/__init__.py'
 * Update conftest.py

### Deprecations

 * Support of Horovod and TF 1.12 for TensorFlow Script Mode. TFS 1.12 support
 * Handle StopIteration in CloudWatch Logs retrieval during training

### Bug fixes

 * Bump version to 1.18.1

### Other changes and improvements

 * Move version definition back to setup.py
 * Supporting inter-container traffic encryption flag
 * Specify task of training/tuning job in Airflow transform/deploy operator
 * Upgrade version to 1.17.0
 * Upgrade to TensorFlow 1.12
 * Update all MXNet integ tests to use the latest version
 * Make include_cls_metadata default to False for everything except Frameworks
 * Add Model.transformer()
 * enable canary for EI supported regions
 * Remove pyYAML dependency.
 * Add missing documentation
 * Update CHANGELOG
 * SM_HPS is worth mentioning
 * Add TFRecord split type to docs
 * Revert appending Airflow retry id to default job name
 * Remove __all__ from __init__.py files
 * Make sure that an arn including 'role' won't pass (#65)
 * Fix readthedocs link.
 * Upgrade version to 1.16.3
 * Update latest version of PyTorch to 1.0
 * Lowercase container hostnames
 * fix quotes
 * move sagemaker_s3_output to model class
 * Append retry id to default Airflow job name to avoid naming collision in retry
 * Fix container path for source files when using local_session
 * Add support for Hyperparameter Tuning Early Stopping
 * Fix requests version to 2.20 for readthedocs.
 * Add readme docs for chainer, pytorch, rl and tensorflow serving.
 * Sklearn documentation
 * fix additional p2 and job/endpoint naming issues
 * Add API doc for Airflow
 * skip p3 hosting tests in lhr
 * narrow requests version bounds
 * update changelog
 * fix tests with incorrect region-skipping code
 * Add a check for S3 paths being incorrectly passed as an entry point
 * Add AugmentedManifestFile & ShuffleConfig support
 * change version range for requests dependency
 * Add AWS Marketplace Integration Tests
 * Remove unnecessary dependency tensorflow
 * Add support for intermediate output to a local directory in local mode.
 * enable ei integ tests
 * fix flaky test
 * increase docker-compose timeout to 120 and ping interval to 5
 * fix region error in test
 * Change 'distribution' to 'distributions' in documentation

### Documentation changes

 * update EI version for TF to 1.12
 * Support VPC config for hyperparameter tuning and bump version to 1.17.2

## 1.0.0

### Breaking changes

 * Reducing test flakiness
 * Bumping up version to 1.18.0 for horovod release

### New features

 * Add 'tuner' to imports in 'sagemaker/__init__.py'
 * Update conftest.py

### Deprecations

 * Support of Horovod and TF 1.12 for TensorFlow Script Mode. TFS 1.12 support
 * Handle StopIteration in CloudWatch Logs retrieval during training

### Bug fixes

 * Bump version to 1.18.1

### Other changes and improvements

 * Move version definition back to setup.py
 * Supporting inter-container traffic encryption flag
 * Specify task of training/tuning job in Airflow transform/deploy operator
 * Upgrade version to 1.17.0
 * Upgrade to TensorFlow 1.12
 * Update all MXNet integ tests to use the latest version
 * Make include_cls_metadata default to False for everything except Frameworks
 * Add Model.transformer()
 * enable canary for EI supported regions
 * Remove pyYAML dependency.
 * Add missing documentation
 * Update CHANGELOG
 * SM_HPS is worth mentioning
 * Add TFRecord split type to docs
 * Revert appending Airflow retry id to default job name
 * Remove __all__ from __init__.py files
 * Make sure that an arn including 'role' won't pass (#65)
 * Fix readthedocs link.
 * Upgrade version to 1.16.3
 * Update latest version of PyTorch to 1.0
 * Lowercase container hostnames
 * fix quotes
 * move sagemaker_s3_output to model class
 * Append retry id to default Airflow job name to avoid naming collision in retry
 * Fix container path for source files when using local_session
 * Add support for Hyperparameter Tuning Early Stopping
 * Fix requests version to 2.20 for readthedocs.
 * Add readme docs for chainer, pytorch, rl and tensorflow serving.
 * Sklearn documentation
 * fix additional p2 and job/endpoint naming issues
 * Add API doc for Airflow
 * skip p3 hosting tests in lhr
 * narrow requests version bounds
 * update changelog
 * fix tests with incorrect region-skipping code
 * Add a check for S3 paths being incorrectly passed as an entry point
 * Add AugmentedManifestFile & ShuffleConfig support
 * change version range for requests dependency
 * Add AWS Marketplace Integration Tests
 * Remove unnecessary dependency tensorflow
 * Add support for intermediate output to a local directory in local mode.
 * enable ei integ tests
 * fix flaky test
 * increase docker-compose timeout to 120 and ping interval to 5
 * fix region error in test
 * Change 'distribution' to 'distributions' in documentation

### Documentation changes

 * update EI version for TF to 1.12
 * Support VPC config for hyperparameter tuning and bump version to 1.17.2

## 1.0.0

### Breaking changes

 * Reducing test flakiness
 * Bumping up version to 1.18.0 for horovod release

### New features

 * Add 'tuner' to imports in 'sagemaker/__init__.py'
 * Update conftest.py

### Deprecations

 * Support of Horovod and TF 1.12 for TensorFlow Script Mode. TFS 1.12 support
 * Handle StopIteration in CloudWatch Logs retrieval during training

### Bug fixes

 * Bump version to 1.18.1

### Other changes and improvements

 * Move version definition back to setup.py
 * Supporting inter-container traffic encryption flag
 * Specify task of training/tuning job in Airflow transform/deploy operator
 * Upgrade version to 1.17.0
 * Upgrade to TensorFlow 1.12
 * Update all MXNet integ tests to use the latest version
 * Make include_cls_metadata default to False for everything except Frameworks
 * Add Model.transformer()
 * enable canary for EI supported regions
 * Remove pyYAML dependency.
 * Add missing documentation
 * Update CHANGELOG
 * SM_HPS is worth mentioning
 * Add TFRecord split type to docs
 * Revert appending Airflow retry id to default job name
 * Remove __all__ from __init__.py files
 * Make sure that an arn including 'role' won't pass (#65)
 * Fix readthedocs link.
 * Upgrade version to 1.16.3
 * Update latest version of PyTorch to 1.0
 * Lowercase container hostnames
 * fix quotes
 * move sagemaker_s3_output to model class
 * Append retry id to default Airflow job name to avoid naming collision in retry
 * Fix container path for source files when using local_session
 * Add support for Hyperparameter Tuning Early Stopping
 * Fix requests version to 2.20 for readthedocs.
 * Add readme docs for chainer, pytorch, rl and tensorflow serving.
 * Sklearn documentation
 * fix additional p2 and job/endpoint naming issues
 * Add API doc for Airflow
 * skip p3 hosting tests in lhr
 * narrow requests version bounds
 * update changelog
 * fix tests with incorrect region-skipping code
 * Add a check for S3 paths being incorrectly passed as an entry point
 * Add AugmentedManifestFile & ShuffleConfig support
 * change version range for requests dependency
 * Add AWS Marketplace Integration Tests
 * Remove unnecessary dependency tensorflow
 * Add support for intermediate output to a local directory in local mode.
 * enable ei integ tests
 * fix flaky test
 * increase docker-compose timeout to 120 and ping interval to 5
 * fix region error in test
 * Change 'distribution' to 'distributions' in documentation

### Documentation changes

 * update EI version for TF to 1.12
 * Support VPC config for hyperparameter tuning and bump version to 1.17.2

## 1.0.0

### Breaking changes

 * Reducing test flakiness
 * Bumping up version to 1.18.0 for horovod release

### New features

 * Add 'tuner' to imports in 'sagemaker/__init__.py'
 * Update conftest.py

### Deprecations

 * Support of Horovod and TF 1.12 for TensorFlow Script Mode. TFS 1.12 support
 * Handle StopIteration in CloudWatch Logs retrieval during training

### Bug fixes

 * Bump version to 1.18.1

### Other changes and improvements

 * Move version definition back to setup.py
 * Supporting inter-container traffic encryption flag
 * Specify task of training/tuning job in Airflow transform/deploy operator
 * Upgrade version to 1.17.0
 * Upgrade to TensorFlow 1.12
 * Update all MXNet integ tests to use the latest version
 * Make include_cls_metadata default to False for everything except Frameworks
 * Add Model.transformer()
 * enable canary for EI supported regions
 * Remove pyYAML dependency.
 * Add missing documentation
 * Update CHANGELOG
 * SM_HPS is worth mentioning
 * Add TFRecord split type to docs
 * Revert appending Airflow retry id to default job name
 * Remove __all__ from __init__.py files
 * Make sure that an arn including 'role' won't pass (#65)
 * Fix readthedocs link.
 * Upgrade version to 1.16.3
 * Update latest version of PyTorch to 1.0
 * Lowercase container hostnames
 * fix quotes
 * move sagemaker_s3_output to model class
 * Append retry id to default Airflow job name to avoid naming collision in retry
 * Fix container path for source files when using local_session
 * Add support for Hyperparameter Tuning Early Stopping
 * Fix requests version to 2.20 for readthedocs.
 * Add readme docs for chainer, pytorch, rl and tensorflow serving.
 * Sklearn documentation
 * fix additional p2 and job/endpoint naming issues
 * Add API doc for Airflow
 * skip p3 hosting tests in lhr
 * narrow requests version bounds
 * update changelog
 * fix tests with incorrect region-skipping code
 * Add a check for S3 paths being incorrectly passed as an entry point
 * Add AugmentedManifestFile & ShuffleConfig support
 * change version range for requests dependency
 * Add AWS Marketplace Integration Tests
 * Remove unnecessary dependency tensorflow
 * Add support for intermediate output to a local directory in local mode.
 * enable ei integ tests
 * fix flaky test
 * increase docker-compose timeout to 120 and ping interval to 5
 * fix region error in test
 * Change 'distribution' to 'distributions' in documentation

### Documentation changes

 * update EI version for TF to 1.12
 * Support VPC config for hyperparameter tuning and bump version to 1.17.2
