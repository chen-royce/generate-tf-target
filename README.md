# Auto-generate TF statement with targets
## Instructions
1. Download a copy of this project locally. Make sure you have Python3 installed.
2. Replace the `input.txt` file with the Terraform code that you are looking to execute. You can copy and paste the entire file in and it'll work.
3. Run `main.py` to generate a `terraform apply` statement targeting the resources/modules that you put in step #2's `input.txt` file.
   1. The default statement generated uses `terraform apply`, but you can also generate a `terraform plan` by switching the `BASE_COMMAND` var in `main.py` to use the value `'terraform plan'`