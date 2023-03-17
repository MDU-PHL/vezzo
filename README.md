# `vezzo`:  a small library to parse version strings from binfie tools

## Background

It is a common pattern when running binfie tools to run checks on the versions 
of the tool's dependencies. For example, the tool might depend on `blastn` being
of version 2.10.0 or higher. This library provides a simple way to parse the 
version from the output of running `blastn -version` and compare it to the minimum
version required. To run the comparison, we use the `semver` [library](https://python-semver.readthedocs.io/en/latest/).

## Usage
The main function provided by the library is `vezzo.verify_from_config`. This 
function takes in the path to a YAML file that specifies the version requirements:

```yaml
- name: blastn
  req_version: ">=2.10.0"
  version_flag: -version
  exit_code: 0

- name: samtools
  req_version: ">=1.16.0"
  version_flag: --version
  exit_code: 0
```

The `name` field is the name of the tool. The `req_version` field that specifies
the requirements in terms of the version of the tool. This takes one the following
format:
    - <1.2.3: the observed version must be less than 1.2.3
    - <=1.2.3: the observed version must be less than or equal to 1.2.3
    - >1.2.3: the observed version must be greater than 1.2.3
    - >=1.2.3: the observed version must be greater than or equal to 1.2.3
    - ==1.2.3: the observed version must be equal to 1.2.3
    - !=1.2.3: the observed version must not be equal to 1.2.3

The `version_flag` field specifies the flag to pass to the tool to get the version
string. This can be empty string, as is the case for `bwa`, which does not have a flag.

The `exit_code` field specifies the exit code that the tool returns when the version 
string is returned. The majority of cases this is 0, but `bwa`, for instance, returns

By specifying all the version requirements in a YAML config file that ships with your
package it is easy to check dependencies and modify requirement all in one location.


