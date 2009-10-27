import txlb
from txlb.util import dist


dist.setup(
    name=txlb.name,
    version=txlb.version,
    description=txlb.description,
    author="Duncan McGreggor, Anthony Baxter",
    author_email="oubiwann@adytum.us",
    url=txlb.projectURL,
    packages=dist.findPackages("txlb"),
    scripts=["bin/txlb.tac"],
    long_description=dist.catReST(
        "docs/PRELUDE.txt",
        "README",
        "docs/DEPENDENCIES.txt",
        "docs/INSTALL.txt",
        "docs/USAGE.txt",
        "docs/PERFORMANCE.txt",
        "docs/HISTORY.txt",
         out=True),
    license="MIT",
    classifiers=[
       "Development Status :: 5 - Production/Stable",
       "Environment :: Web Environment",
       "Environment :: No Input/Output (Daemon)",
       "License :: OSI Approved :: Python Software Foundation License",
       "Operating System :: POSIX",
       "Operating System :: MacOS :: MacOS X",
       "Operating System :: Microsoft",
       "Programming Language :: Python",
       "Intended Audience :: System Administrators",
       "Intended Audience :: Developers",
       "Topic :: Internet",
       "Topic :: System :: Networking",
    ]

)
