# 🔑 Random Password Generator

A simple command-line tool for generating strong, random passwords. The user can specify the desired length, and the script will create a password using a mix of uppercase letters, lowercase letters, numbers, and special symbols.

## Features

* **Custom Length**: The user can define the exact length of the generated password.
* **Strong Character Set**: Uses a comprehensive set of characters from Python's `string` module (`ascii_letters`, `digits`, `punctuation`) for high entropy.
* **Secure Randomness**: Utilizes Python's `random.choices` for generating the sequence of characters.
* **User-Friendly**: A simple prompt and a "generating" animation make it easy to use.

## How to Use

1.  Ensure you have Python installed.
2.  Save the code as a `.py` file (e.g., `password_generator.py`).
3.  Run the script from your terminal:
    ```sh
    python password_generator.py
    ```
4.  When prompted, enter the number of characters you want in your password and press Enter.
5.  The script will display your new, randomly generated password.

### Example Session

```sh
> python password_generator.py
---------- RANDOM PASSWORD GENERATOR ----------
How many characters you need in this password?
16
Generating password...
Your password: &H8j@#v!Lp$5sW2k
```
