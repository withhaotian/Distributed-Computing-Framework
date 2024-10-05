# Distributed Computing Framework

This repo is a distributed computing and communication framework by Python based on bluelet. It provides a simple and efficient way to write and run parallel programs on a cluster of machines (nodes) in a distributed environment, e.g., IoT systems or edge computing.

## How to use
    root_dir/
    │
    ├── src/
    │   ├── communication/
    │   │   └── networking.py
    │   │
    │   │── config/
    │   │   └── configs.py
    │   │
    │   │── data/               # datasets
    │   │── models/             # models (e.g., ML)
    │   │── scheduler/          # scheduler algo
    │   │── top/
    │   │   │── client.py
    │   │   │── follower.py
    │   │   └── leader.py
    │   │
    │   └── utils/              # utility functions
    │
    ├── tests/
    │   └── test_xxx.py         # test files
    │
    │── README.md

You can tailor the framework to your specific needs by modifying the code in the `src` directory. 

The `tests` directory contains some test files to verify the correctness of the framework.

## Requirements
Before developement and extending the functionality of this framework, you need to install the following package:

    pip install bluelet

## Statement
This repo is only used for educational purposes and should not be used in production environments.

## Contact
If you have any questions or suggestions, please contact me at: withhaotian [at] gmail [dot] com.