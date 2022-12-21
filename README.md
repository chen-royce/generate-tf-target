# 🎯 Auto-generate TF statement with targets
## Instructions
1. Download a copy of this project locally. Make sure you have Python3 installed.
2. Replace the `input.txt` file with the Terraform code that you are looking to execute. You can copy and paste the entire file in and it'll work.
3. Run `main.py` to generate a `terraform apply` statement targeting the resources/modules that you put in `input.txt` file as specified in step 2.

### Note
The default statement generated uses `terraform apply` However, you can also generate a `terraform plan` by switching the `BASE_COMMAND` var in `main.py` to use the value `'terraform plan'`