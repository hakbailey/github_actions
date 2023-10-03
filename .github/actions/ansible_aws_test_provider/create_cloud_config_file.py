#!/usr/bin/python
"""Script to write AWS credentials from env to cloud config INI file."""

import logging
import os


FORMAT = "[%(asctime)s] - %(message)s"
logging.basicConfig(format=FORMAT)
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)


def main() -> None:
    """Create cloud-config-aws.ini file for ansible-test."""
    cloud_config_file = os.environ["ANSIBLE_TEST_CLOUD_CONFIG_FILE"]
    access_key = os.environ["AWS_ACCESS_KEY_ID"]
    secret_key = os.environ["AWS_SECRET_ACCESS_KEY"]
    session_token = os.environ["AWS_SESSION_TOKEN"]
    aws_credentials = [
        "[default]",
        f"aws_access_key: {access_key}",
        f"aws_secret_key: {secret_key}",
        f"security_token: {session_token}",
        "aws_region: us-east-1",
        f"ec2_access_key: {access_key}",
        f"ec2_secret_key: {secret_key}",
        "ec2_region: us-east-1",
    ]
    logger.info("writing aws credentials into file => %s", cloud_config_file)
    with open(cloud_config_file, mode="w", encoding="utf-8") as file_writer:
        file_writer.write("\n".join(aws_credentials))


if __name__ == "__main__":
    main()
