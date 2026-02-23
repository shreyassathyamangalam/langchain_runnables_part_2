# langchain_runnables_part_2

**langchain-runnables2** is a Python package that provides a set of powerful utilities for working with LangChain, a popular library for building applications that utilize language models. This package extends the functionalities of LangChain with various runnable components designed to streamline the process of creating complex workflows.

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Files Overview](#files-overview)
- [Contributing](#contributing)
- [License](#license)

## Features

- **Runnable Branch**: Run tasks in a specified branch based on conditions.
- **Runnable Lambda**: Create and execute small anonymous functions seamlessly.
- **Runnable Parallel**: Execute multiple tasks in parallel for enhanced performance.
- **Runnable Passthrough**: Pass data through without modification, useful for debugging workflows.
- **Runnable Sequence**: Chain multiple tasks sequentially.

## Installation

To install `langchain-runnables2`, ensure you have Python 3.12 or higher installed, then run the following command:

```bash
pip install langchain-runnables2
```

You can also install it directly from the repository:

```bash
git clone https://github.com/yourusername/langchain_runnables_part_2.git
cd langchain_runnables_part_2
pip install -e .
```

## Usage

Here's a basic example of how to use the various runnables in this package:

```python
from runnable_branch import RunnableBranch
from runnable_lambda import RunnableLambda
from runnable_parallel import RunnableParallel
from runnable_passthrough import RunnablePassthrough
from runnable_sequence import RunnableSequence

# Sample usage for each runnable goes here
```

For detailed usage information, please check the documentation linked in this repository.

## Files Overview

- **.gitignore**: Specifies files and directories that should be ignored by Git.
- **.python-version**: Specifies the Python version for your environment setup.
- **README.md**: This file, containing project information.
- **pyproject.toml**: Defines project metadata and dependencies.
- **runnable_branch.py**: Contains implementation of the Runnable Branch functionality.
- **runnable_lambda.py**: Contains implementation of the Runnable Lambda functionality.
- **runnable_parallel.py**: Contains implementation of the Runnable Parallel functionality.
- **runnable_passthrough.py**: Contains implementation of the Runnable Passthrough functionality.
- **runnable_sequence.py**: Contains implementation of the Runnable Sequence functionality.
- **uv.lock**: Lock file generated for package dependencies.

## Contributing

Contributions are welcome! If you'd like to contribute, please fork the repository and submit a pull request. Make sure to follow the [code of conduct](CODE_OF_CONDUCT.md).

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

Thank you for your interest in `langchain-runnables2`. We hope this package enhances your experience with LangChain and helps you build more efficient workflows!