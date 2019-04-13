#!/usr/bin/env python3


import sys
import os
import configparser
import MySQLdb
import datetime
import time
import textwrap
import texttable
import re
import xlsxwriter
import csv

### Importable repo helper functions ###

def add_repo(project_id,git_repo,db,cursor):

	# Adds a new repo to a specific project
	#
	# project_id: Integer corresponding to an ID in the 'projects' table
	# git_repo: A string containing the full URI to a git repo
	# db: A database connection object
	# cursor: A database cursor

	# Does not return anything

def delete_repo(git_repo,db,cursor):

	# Removes an uninitizliaed git repo, or marks it for deletion if it has
	# already been cloned
	#
	# git_repo: Integer corresponding to an ID in the 'repos' table
	# db: A database connection object
	# cursor: A database cursor

	# Does not return anything 
	db.commit()


### Importable project helper functions ###

def add_project(name,description,website,db,cursor):

	# Adds a new project
	#
	# name: String containing project's name
	# description: String describing project (can be blank)
	# website: String with project's website (can be blank)
	# db: A database connection object
	# cursor: A database cursor

	# does not return anything, it just does a database commit. 
	db.commit()


def get_setting(setting,db,cursor):

	# Helper to quickly return a setting
	#
	# setting: String corresponding to a 'setting' in the settings table
	# db: A database connection object
	# cursor: A database cursor

	return cursor.fetchone()['value']


#-----------------------------------------------------------------------------#
#            Below this point, everything is specific to facade.py            #
#-----------------------------------------------------------------------------#

### General helper functions ###

### Main functions ###

def _manage_projects():

	# Find out if there are any projects to display


		# If there are projects already defined, display them



			# Add a project


			# Name is mandatory


			# Description and website are optional

			description = input("Description (optional): ").strip()
			website = input("Website (optional): ").strip()

			# Edit a project

			print("\n................\nModify a project\n................\n")

			# Proceed only if there is a project to modify
			if not existing_projects:
				return

			# Collect the project ID to modify



def _list_repo_status(request_id=0,show_id=0):

	# List repo statuses. Used by both the Repo main menu item as well as repo
	# display for specific projects.


	# Narrow down the query to a specific project

	# Print out the repos for each project

		# Select project-specific repo data



			# Normally when viewing a repo, it's unnecessary to show the repo's
			# ID.  However, if you're editing a repo you need to see it, so
			# show_id toggles whether or not the ID is displayed.  This is only
			# ever used in conjunction with request_id.


			# If there's no fetch status, the repo must be new


			# If there's no analysis status, the data must be unanalyzed


#		print(repo status)

