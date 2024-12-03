# Password Hashing and Management

This project provides a simple command-line interface for password hashing, verification, generation, and strength checking using the Argon2 hashing algorithm.

## Features

- **Hash a Password**: Securely hash a password using Argon2.
- **Verify a Password**: Verify a provided password against a stored hashed password.
- **Generate a Random Password**: Generate a strong random password of specified length.
- **Check Password Strength**: Check the strength of a password based on various criteria.

## Requirements

- Python 3.x
- `argon2-cffi` library

## Installation

1. Clone the repository:

   ```sh
   git clone https://github.com/Muhammadkafaby/Password-Hashing.git
   cd password-hashing
   ```

2. Install the required dependencies:
   ```sh
   pip install -r requirements.txt
   ```

## Usage

Run the script:

```sh
python

hashing.py


```

You will be presented with a menu to choose from the following options:

1. Hash a password
2. Verify a password
3. Generate a random password
4. Check password strength
5. Exit

## Example

### Hash a Password

```sh
Enter the password to hash: [your_password]
Hashed Password: [hashed_password]
```

### Verify a Password

```sh
Enter the stored hashed password: [stored_hashed_password]
Enter the password to verify: [your_password]
Password is valid: True/False
```

### Generate a Random Password

```sh
Enter the length of the random password: 12
Random Password: [random_password]
```

### Check Password Strength

```sh
Enter the password to check strength: [your_password]
Password is strong: True/False
```

## License

This project is licensed under the MIT License.

```

Replace `https://github.com/yourusername/password-hashing.git` with the actual URL of your repository. This

README.md

 provides an overview of the project, installation instructions, usage examples, and licensing information.
```
