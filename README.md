# Test Automation Framework - Playwright & Python

Welcome to the Test Automation Framework. This framework is designed to simplify the process of writing, running, and managing automated tests.

## Introduction

This Test Automation Framework based on Playwright and Python provides a robust and scalable solution for automating the testing of web applications. It uses pytest as the test runner and integrates seamlessly with CI/CD pipelines.

## Features

- Easy setup and configuration
- Supports multiple browsers
- Detailed test reporting with Allure
- CI/CD integration
- Modular and maintainable code structure
- Customizable test settings

## Installation

To get started, clone the repository and install the necessary dependencies.

```bash
git clone https://github.com/dalaian/full_me.git
cd full_me
pip install poetry
poetry install
```

## Configuration
Configuration settings for the framework can be found in the config directory. Update the config.yaml file to suit your needs.

```yaml
# config.yaml
url: http://example.com
CI: True
```

## Running Tests
You can run tests using the following commands:
```bash
# Run all tests
poetry run pytest

# Run tests with a specific marker
poetry run pytest -m sanity

# Run test in parallel
poetry run pytest --numprocesses 2

# Generate Allure reports
poetry run pytest --alluredir=allure-results
```

## Writing Tests
Tests are written using the pytest framework. Place your test files in the tests directory. Here's an example of a basic test:
```python
@pytest.mark.sanity
def test_default_login(login):
    page = login
    expect(page.get_by_text("Swag Labs")).to_be_visible()
```

### Playwright Codegen Feature
Playwright offers a codegen feature that allows you to generate scripts by recording your interactions with the browser. This can significantly speed up the creation of automated tests.

To use the codegen feature, run the following command:
```bash
poetry run playwright codegen https://www.saucedemo.com/
```

## Directory Structure
The directory structure of the framework is organized as follows:
```plaintext
full_me/
│
├── .github/
│   └── workflows/
│       └── sanity-testing.yml
├── .vscode/
│   └── settings.json
├── config/
│   └── config.yaml
├── tests/
│   └── feature_a
|       ├── test_abc.py
├── utils/
│   └── config.py
│   └── email.py
├── .gitignore
├── conftest.py
├── pyproject.toml
└── README.md
```

## Contributing
We welcome contributions to the Test Automation Framework! Please follow these steps to contribute:

1. Fork the repository
2. Create a new branch (git checkout -b feature-branch)
3. Commit your changes (git commit -am 'Add new feature')
4. Push to the branch (git push origin feature-branch)
5. Create a new Pull Request


## Contact
For any questions or support, please open an issue or contact the repository owner at dalaian@outlook.com


## Notes
- Ensure you have the required secrets (`EMAIL_PASSWORD` and `GITHUB_TOKEN`) set up in your GitHub repository.
- The workflow is configured to always try to deploy the Allure report even if previous steps fail.