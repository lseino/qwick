#get latest ubuntu ami
data "aws_ami" "ubuntu" {
  most_recent = true

  filter {
    name   = "name"
    values = ["ubuntu/images/hvm-ssd/ubuntu-focal-20.04-amd64-server-*"]
  }

  filter {
    name   = "virtualization-type"
    values = ["hvm"]
  }

  owners = ["099720109477"] # Canonical
}

module "ec2_instance" {
  source  = "terraform-aws-modules/ec2-instance/aws"
  version = "~> 3.0"

  name = "qwick_ubuntu"

  ami                    = data.aws_ami.ubuntu.id
  instance_type          = "t2.medium"
  key_name               = "qwick"
  monitoring             = true

  tags = {
    Terraform   = "true"
    Environment = "dev"
  }
}

output "public_ip" {
    value = module.ec2_instance.public_ip
}