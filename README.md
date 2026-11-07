# Password Generator (Python)

A simple Python script that generates and prints a random 12-character password each time it runs.

## Features

- Uses uppercase and lowercase English letters, digits, and punctuation as the character pool.
- Generates a password with a fixed length of 12 characters.
- Runs without installing any additional packages.

## Requirements

- Python 3

The script uses Python's built-in `random` and `string` modules.

## How to run

1. Download or clone this repository.
2. Open a terminal in the folder containing `Password Generator.py`.
3. Run:

```bash
python3 "Password Generator.py"
```

On systems where Python 3 is available as `python`, use:

```bash
python "Password Generator.py"
```

## Example output

```text
Your secure random password is: aB7!qR2@xZ9#
```

The generated password will usually differ on each run. The example above is illustrative.

## How it works

1. Combines `string.ascii_letters`, `string.digits`, and `string.punctuation` into one character pool.
2. Calls `random.choice(characters)` 12 times to select individual characters. Characters may repeat.
3. Joins the selected characters into one string and prints it.

## Limitations

- Password length is fixed at 12 characters.
- A generated password is not guaranteed to contain every character type.
- Passwords are printed to the terminal; the script does not save them to a file.
- Although the output message says “secure,” Python's `random` module is not designed for security-sensitive password generation. This version is suitable as a learning exercise. Use the `secrets` module for passwords intended to protect real accounts.

## Possible improvements

- Replace `random.choice` with `secrets.choice`.
- Allow the user to choose the password length.
- Add options for allowed characters.
- Add validation if every selected character type must be included.
