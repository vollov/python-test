from invoke import task
import pytest

@task()
def clean():
    '''Clean build directory.'''
    print 'Cleaning build directory...'

@task(clean, help={'name': "Name of the person to say hi to."})
def hi(name):
    print("Hi %s!" % name)

@task
def all():
    pytest.main()


@task(clean)
def unit():
    pytest.main('tests/unit')
