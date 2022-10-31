Start of transcript. Skip to the end.
Given the concerns around data security and privacy, especially in public cloud environments,
encryption plays a key role, and is often referred to as the last line of defense, in
a layered security model.
This protection not only encrypts data, but also provides robust data access control,
key management, and certificate management.
In this video, we will take a closer look at cloud encryption.
Encryption is defined as scrambling data in a way that makes it illegible.
There are two parts to an encryption system—the encryption algorithm and the decryption key.
The encryption algorithm defines the rules by which data will be transformed so that
it becomes illegible; and The decryption key defines how the encrypted
data will be transformed back to legible data.
Encryption ensures that only authorized users have access to sensitive data, and when accessed
or intercepted without authorization, data is unreadable and meaningless.
Cloud providers offer various cloud encryption services.
This could be limited encryption of data that is identified as sensitive or end-to-end encryption
of all data uploaded to the cloud.
Data is encrypted upon receipt, and encryption keys are passed to the customers to decrypt
data when needed.
Keys need to be managed securely.
If you lose your keys, you will not be able to read your data.
Data needs protection in three states—at rest, in transit, and when it is in use.
Encryption at rest protects data while it is physically stored in a database or the
storage layer.
Depending on the application and business requirements, there could be multiple options
for encrypting data at rest, such as encryption for block and file storage, built-in encryption
in object storage, and database encryption services.
Encryption in transit protects data while it is transmitted from one location to another.
Encryption in transit includes encrypting the data before transmission, authenticating
endpoints, and decrypting and verifying data on arrival.
Secure Sockets Layer (or SSL) and Transport Layer Security (TLS) are commonly used protocols
for encryption in transit.
They are not only used when accessing websites securely but also for data moving between
servers and services within the cloud.
Encryption in use protects data when it is in use in memory for computations.
It allows computations to be performed on encrypted text without needing to decrypt
the data.
Cloud storage encryption could be server-side or client-side.
Server-side encryption occurs after cloud storage receives your data, but before the
data is written to disk and stored.
For server-side encryption, you can either: Create and manage your own encryption keys,
known as Customer-supplied encryption keys; or You can generate and manage your encryption
keys using key management services offered by the cloud storage provider, known as Customer-managed
encryption keys.
Client-side encryption occurs before data is sent to cloud storage.
This way, users can utilize encryption keys and algorithms that are not visible to the
cloud provider, making it virtually impossible for cloud providers to decrypt hosted data.
Given that a majority of enterprises today operate in multi-cloud environments, there
is a need to implement a singular data protection strategy across an enterprise’ on-premise,
hybrid, and multi-cloud deployments.
Some cloud providers offer multi-cloud data encryption services with a range of features
such as data access management, integrated key management, and sophisticated encryption
that combine to deliver the scalability and flexibility to help protect the most sensitive
workloads—across the enterprise—regardless of where the data resides.
Using a multi-cloud data encryption console, you can define and manage access policies,
create, rotate, and manage encryption keys, and aggregate access logs.
Encryption does not eliminate data security risk—it separates the security risk from
the data itself by moving security to the encryption keys.
These keys need to be managed and protected against threats in order to keep the data
secure.
Key Management Services offered by some cloud providers help perform life cycle management
for encryption keys that are used in cloud services or customer-built applications.
They enable customers to encrypt sensitive data at rest and to easily create and manage
the entire lifecycle of cryptographic keys that are used to encrypt data.
Since the keys remain in possession of the customer, the data is protected from cloud
service providers as well as from other users.
Some of the best practices for encryption key management include:
Storing encryption keys separately from the encrypted data.
Taking key backups offsite and auditing them regularly.
Refreshing the keys periodically.
Implementing multi-factor authentication for both the master and recovery keys.
In the next video, we will learn about cloud monitoring and its benefits.
End of transcript. Skip to the start
