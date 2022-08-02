from setuptools import setup, find_packages
import io

setup(
    name = "function_controler",     
    version = "0.0.2", 
    keywords = ["pip", "function_controler","running time","control"],			
    description = "Control the maximum running time of a function.",	
    long_description=io.open("README.md", "r", encoding='utf-8').read(),
    long_description_content_type="text/markdown",
    license = "MIT Licence",		

    url = "https://github.com/dongshuyan/function_controler", 
    author = "sauterne",			
    author_email = "ssauterne@qq.com",

    packages = find_packages(),
    include_package_data = True,
    platforms = "any",
    install_requires = ["loguru"] 
)