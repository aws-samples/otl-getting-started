
AWS Outposts Test Lab
=====================

Contents
========

* [What is the Outposts Test Lab?](#what-is-the-outposts-test-lab)
	* [Participation Criteria](#participation-criteria)
* [Getting Started](#getting-started)
	* [Pre-Onboarding](#pre-onboarding)
	* [Testing Environment](#testing-environment)
* [Resources](#resources)
	* [Local Gateway Configuration](#local-gateway-configuration)
	* [Terraform Module Library](#terraform-module-library)
* [FAQ](#faq)

# What is Outposts Test Labs?

Outposts Test Labs (OTL) is a program that enables AWS customers and partners to remotely test their solutions on real Outpost racks. OTL has limited capacity, and participants must submit requests for access to their AWS representative (Account Manager, Partner Manager, TAM, etc.) to be considered for a test slot. OTL is intended for proof-of-concept work, so test slots are typically 2-3 weeks long.

## Participation Criteria

- Applications must be pre-validated in an AWS region.
- Participants are responsible for providing a test plan with success criteria prior to testing.
- No production data, or other sensitive data, is used during testing.

This guide describes how to set up account and networking access for testing. Your participation in this program is governed by your Agreement with AWS and the AWS Service Terms. In particular, please note that your participation in this preview is subject to the Universal and Beta Service Participation of the AWS Service Terms and is confidential. Please do not discuss the features, functionality, or documentation related to this feature with any parties (individuals or businesses) that are not authorized by Amazon Web Services.

***``Important:``***
- Please do not post questions and comments to the general AWS forums as this program is not publicly released. You can send your questions and feedback to your AWS representative.

# Getting Started

## Pre-Onboarding

- Identify all members of your team who will be performing hands-on-keyboard testing and provide their emails to your AWS representative. AWS will coordinate an onboarding call between your testers, your AWS account team, and the OTL administrators.
- Request an OTL test plan template from your AWS account representative and fill it out. The test plan is intended to ensure that it is feasible to complete your test given the parameters of OTL's environment.

## Testing Environment

- During the onboarding call, testers will receive an AWS SSO login that will allow them administrator access to an AWS-owned temporary testing account. The SSO login portal is available here: https://outposts-test-labs.awsapps.com/start
- Testers will also receive access to a shared Amazon Chime chat room, where they will be able to collaborate with their AWS account representatives and the OTL administrators. 
- The temporary test account will have an OTL Outpost shared to it via RAM. The Outpost will appear in the test account as though the test account owns the Outpost. Testers will be able to launch AWS infrastructure in the test account, including resources homed to the Outpost.

### Outposts Documentation

- Outposts documentation is available here: https://docs.aws.amazon.com/outposts/
- How to launch an EC2 instance on an Outpost: https://docs.aws.amazon.com/outposts/latest/userguide/launch-instance.html

# Resources

## Local Gateway Configuration

- In OTL we can route traffic from a separate VPC through the Local Gateway (LGW) of the test Outpost. This setup allows testers to simulate a connection between their Outpost-hosted application and on-premises resources.
- Steps to set up this connectivity:
    - Create a VGW and attach it to your VPC. Enable route propagation on your subnets' route tables.
    - Request a Direct Connect (DX) Gateway ID from the OTL administrators. 
    - Use the Direct Connect console to initiate a sharing request to associate the VGW with the DX gateway. Input your VPC's CIDR range as the prefix you would like to be advertised through the DX gateway.
    - Notify the OTL administrators that you have initiated the sharing request. The OTL administrators will accept the sharing request. 
    - Once the shared connection comes up, it should be possible to ping from instances in your VGW VPC to instances in LGW-associated subnets on the Outpost.

## Terraform Module Library

Several Terraform Modules have been written for OTL and can be accessed here: https://github.com/aws-samples/otl-service-launcher/

# FAQ

- I stumbled on this page by accident, but the Lab sounds interesting! How do I get access?
    - The Lab is intended only for customers and partners who have been selected to participate in the Outposts Testing program.
        - But I have a really cool application that I would love to test in the lab. Can you make an exception?
            - Maybe? Contact your AWS Representative (Account Manager, Partner Manager, TAM, Etc.) for more information on the OTL program.
- Once I am in the Lab, how will I contact the OTL Team?
    - During onboarding, you will be given access to a virtual meeting room hosted by [Amazon Chime](https://app.chime.aws).
