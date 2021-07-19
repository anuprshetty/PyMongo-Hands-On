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

## References

- [MongoDB documentation](https://docs.mongodb.com/)
- [MongoDB Update Operators](https://docs.mongodb.com/manual/reference/operator/update/)
