# Python
#
# This file is rendered with mdutils. https://github.com/didix21/mdutils
#
# MIT License: (C) 2018 Dídac Coll
#
# To use this script, first use pip to install mdutils:
# Use pip to install mdutils:
#    $ pip install mdutils
#
# And then run the script:
#    $ python3 README.py
#



from mdutils.mdutils import MdUtils
from mdutils import Html

mdFile = MdUtils(file_name='../README.md', title='AWS Outposts Test Lab')

mdFile.new_header(level=1, title='What is the Outposts Test Lab?')  # style is set 'atx' format by default.

#mdFile.new_paragraph("[![Join the chat at https://gitter.im/otl-getting-started/community]"
#                     "(https://badges.gitter.im/otl-getting-started/community.svg)]"
#                     "(https://gitter.im/otl-getting-started/community?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge)")

mdFile.new_paragraph("Outposts Test Lab is a program that enables customers "
                     "and partners to test their solutions on Outposts capacity, "
                     "on Outpost racks that are managed by the AWS Outposts team. "
                     "The goal of this program is to give a select set of customers "
                     "access to capacity on Outposts to ensure that their cloud-based "
                     "solutions.")

mdFile.new_paragraph("Note:", bold_italics_code='bic')
items = ["These directions are intended only for customers and partners who have been selected to participate in the Outposts Testing program."]
mdFile.new_list(items)
mdFile.new_paragraph()

# Available Features
mdFile.new_header(level=2, title="Participation Criteria")

items = ["Applications must be validated in an AWS region today",
         "Participants are responsible for providing a test plan with success criteria prior to testing",
         "No production data, or other sensitive data, is used during testing on the Outpost"]
mdFile.new_list(items)

mdFile.new_paragraph("This guide describes how to set up account and networking access for testing. "
                     "Your participation in this program is governed by your Agreement with AWS and the "
                     "AWS Service Terms. In particular, please note that your participation in this preview "
                     "is subject to the Universal and Beta Service Participation of the AWS Service Terms and "
                     "is confidential. Please do not discuss the features, functionality, or documentation related "
                     "to this feature with any parties (individuals or businesses) that are not authorized by Amazon Web Services.")

mdFile.new_paragraph("Important:", bold_italics_code='bic')

items = ["Please do not post questions and comments to the general AWS forums as this program is not publicly released yet. "
         "You can send your questions and feedback to your AWS representative.",
         "During the private beta, you agree not to use this feature for production traffic."]
mdFile.new_list(items)

mdFile.new_paragraph()

mdFile.new_header(level=1, title="Getting Started")

mdFile.new_paragraph("Before your team is granted access to Outposts capacity, we will need to capture account and networking information.")

mdFile.new_header(level=2, title="Pre-Onboarding")

items = ["Identify an acount that you have **STS:AssumeRole** permission in. We will use this accont "
         "to configure a cross-account role. You will use this role to access the console / cli in the OTL account",
         "During the private beta, you agree not to use this feature for production traffic"]
mdFile.new_list(items)

mdFile.new_header(level=2, title="Testing Environment")

mdFile.new_paragraph("By default, the lab will be pre-configured with the following attributes:")

items = ["VPC",
            ["OTL VPC with one subnet residing on the Outpost",
             "This VPC is not fully configured",
             "This VPC assigns public IPs and routes all traffic through IGW"],
         "Subnet",
            ["A subnet as been created on the Outpost"
             "This subnet has been associated with the AWS Outposts Account"]
        ]
mdFile.new_list(items)


mdFile.new_header(level=3, title="Outposts Documentation")

mdFile.new_paragraph("Outposts specific documentation is available here: https://docs.aws.amazon.com/outposts/")


mdFile.new_header(level=1, title="Resources")

mdFile.new_header(level=2, title="Local Gateway Configuration")

items = ["In OTL we can route traffic from a vpc in your account over the LGW "
            "of the outpost. If this setup is desirable to you follow the instructions below",
            ["Create VGW and attach to your VPC",
             "Request association of your VGW to OTL DX GW (Request DX GW from OTL Operators)",
             "Provide OTL Operators with CIDR block of your VPC"]
        ]
mdFile.new_list(items)

mdFile.new_header(level=2, title="Terraform Module Library")

mdFile.new_paragraph("Several Terraform Modules have been written for OTL and can be accessed here: https://github.com/Outposts-Test-Lab/otl-service-launcher")

mdFile.new_header(level=1, title="FAQ")

items = ["I stumbled on this page by accident, but the Lab sounds interesting! How do I get access?",
            ["The Lab is intended only for customers and partners who have been selected to participate in the Outposts Testing program.",
                ["But I have a really cool application that I would love to test in the lab. Can you make an exception?",
                    ["Maybe? Contact your AWS Representative (Account Manager, Partner Manager, TAM, Etc.) for more information on the OTL program."],
                ],
            ],
         "I don't seem to be able to create any IAM Roles! I need these roles to test my application. Can I be given access?",
            ["The creation of IAM roles is prohibited in OTL.  However, the OTL team can create them for you."],
         "Once I am in the Lab, how will I concact the OTL Team?",
            ["During onboarding, you will be given access to a virtual meeting room hosted by [Amazon Chime](https://app.chime.aws)."],
         "Why do you need my account number?",
            ["During onboarding, we will grant [sts:AssumeRole](https://docs.aws.amazon.com/STS/latest/APIReference/API_AssumeRole.html) access to this account so that you can access the Outposts Test Lab."]
        ]
mdFile.new_list(items)

mdFile.new_header(level=1, title="Hello Rohan")

# Create a table of contents
mdFile.new_table_of_contents(table_title='Contents', depth=2)
mdFile.create_md_file()