# PyMongo-Hands-On

PyMongo is a Python distribution containing tools for working with MongoDB, and is the recommended way to work with MongoDB from Python.

## Commands

python -m pip install pymongo[srv]

## Versions

- pymongo==3.12.0
- dnspython==1.16.0

## SQL to NoSQL mapping

| SQL              | NoSQL                     |
|------------------|---------------------------|
| cluster/instance | cluster/instance          |
| db               | db                        |
| table            | collection                |
| row              | document/post(dictionary) |
| field            | key                       |
| value            | value                     |

## URL Encoding

- URL encoding is a mechanism for translating unprintable or special characters to a universally accepted format by web servers and browsers.
- The encoding of information can be applied to Uniform Resource Names (URNs), Uniform Resource Identifiers (URIs) and Uniform Resource Locators (URLs), and selected characters in the URL are replaced by one or more character triplets comprised of the percent character and two hexadecimal digits.
- The hexadecimal digits in the character triplets represent the numerical value of the characters that are replaced.
- URL encoding is widely used in HTML form data submission in HTTP requests.
- URL encoding is also known as percent-encoding.
- Ex: # character is replaced by %23

## References

- [MongoDB documentation](https://docs.mongodb.com/)
- [MongoDB Update Operators](https://docs.mongodb.com/manual/reference/operator/update/)
- [PyMongo Documentation](https://pymongo.readthedocs.io/en/stable/)
