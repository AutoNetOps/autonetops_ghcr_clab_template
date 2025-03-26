#!/usr/bin/env python3

import click
import subprocess
import os
import yaml

@click.command()
@click.option('--bashrc', type=click.Path(exists=True), help='Path to YAML file containing lines to append to .bashrc')
@click.option('--run', type=click.Path(exists=True), help='Path to YAML file containing lines with commands to run')
def postCreate(bashrc, run):
    """
    A tool to run scripts and append lines to .bashrc from a YAML file.

    Options:
        --yaml     Path to a YAML file containing lines to append to .bashrc (optional)

    Usage examples:
        ./postCreate.py --bashrc lines.yaml
        ./postCreate.py --run lines.yaml
    """

    # Handle line appending from YAML
    if bashrc:
        try:
            # Read the YAML file
            with open(bashrc, 'r') as f:
                lines_to_append = yaml.safe_load(f)
                if not lines_to_append:
                    click.echo("No lines found in YAML file.")
                    return

            # Append lines to .bashrc
            bashrc_path = os.path.expanduser("~/.bashrc")
            with open(bashrc_path, 'a') as f:
                for line in lines_to_append:
                    f.write(line + "\n")
            click.echo(f"Appended {len(lines_to_append)} lines from {yaml} to {bashrc_path}")
        except FileNotFoundError:
            click.echo(f"Error: YAML file {yaml} not found.", err=True)
        except yaml.YAMLError as e:
            click.echo(f"Error parsing YAML file: {e}", err=True)
        except Exception as e:
            click.echo(f"Error appending to .bashrc: {e}", err=True)
    else:
        click.echo("No YAML file provided. Skipping line appending.")

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