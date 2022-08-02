from setuptools import setup, find_packages

setup(
    name = "function_controler",     
    version = "0.0.1", 
    keywords = ["pip", "function_controler","running time","control"],			
    description = "Control the maximum running time of a function.",	
    long_description = "Control the maximum running time of a function. Referred to the program of yibeishanguangmiao.",
    license = "MIT Licence",		

    url = "https://github.com/dongshuyan/function_controler", 
    author = "sauterne",			
    author_email = "ssauterne@qq.com",

    packages = find_packages(),
    include_package_data = True,
    platforms = "any",
    install_requires = ["loguru"] 
)