import subprocess


def terraform_init(command):
    process = subprocess.run(command , shell =True ,  stdout=subprocess.PIPE , stderr=subprocess.PIPE)
    print(process.stdout.decode())
    print(process.stderr.decode())


directory = r"C:\Users\Megha.rawat\Downloads\MEGHA\PROJECT\PYTHON\terra_automate\Wanderlust-Mega-Project\terraform"
command = f'terraform -chdir="{directory}" plan'
terraform_init(command);    