# Command list




## Encrypting file to make a vault
### Step 1: Make a file with secret password
Make a file `pass.key` in your project

Enter your password there

Add this file in your `.gitignore` file

### Step 2: Export pass.key in your global variable
```sh
export DEFAULT_VAULT_PASSWORD_FILE=pass.key
```
### Step 3: Make a yml file
```yml
my_var: my_value
my_var2: my_value2
```
### Step 4: Make this file a vault
```sh
ansible-vault encrypt pass.yml --vault-password-file $DEFAULT_VAULT_PASSWORD_FILE

```

to be continu ...