#!/usr/bin/env python3

import click
import subprocess
import os
import yaml

@click.command()
@click.option('--run', type=click.Path(exists=True), help='Path to YAML file containing lines with commands to run')
def postCreate(run):
    """
    A tool to run scripts and append lines to .bashrc from a YAML file.

    Options:
        --yaml     Path to a YAML file containing lines to append to .bashrc (optional)

    Usage examples:
        ./postCreate.py --bashrc lines.yaml
        ./postCreate.py --run lines.yaml
    """

    if run:
        try:
            # Read the YAML file
            with open(run, 'r') as f:
                commands_to_run = yaml.safe_load(f)
                if not commands_to_run:
                    click.echo("No commands found in YAML file.")
                    return

            # Run commands
            for command in commands_to_run:
                subprocess.run(command, shell=True, check=True)
        except FileNotFoundError:
            click.echo(f"Error: YAML file {run} not found.", err=True)
        except yaml.YAMLError as e:
            click.echo(f"Error parsing YAML file: {e}", err=True)
        except subprocess.CalledProcessError as e:
            click.echo(f"Error running command: {e}", err=True)
        except Exception as e:
            click.echo(f"Error running commands: {e}", err=True)
if __name__ == '__main__':
    postCreate()