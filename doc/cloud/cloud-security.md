[Music]
Hi, I'm Nataraj Nagaratnam, and I'm from
IBM Cloud. Traditionally when you deploy
an application, you have the entire data
center, the servers that you run - you're
responsible for all of it. In the cloud
model, that's a shared responsibility
between you and the cloud provider. In a
shared responsibility model, you need to
rethink security; on what your
responsibility is, and what cloud
provider's responsibility is. Let's take
platform as a service as an example. When
you look at PaaS, you're building
applications, migrating data to the cloud,
and building applications, running them on
the cloud. So you're responsible for
securing the applications, the workload,
and the data, while the cloud provider is
responsible for managing the security of
the platform - so that it's compliant, it's
secured from the perspective of network,
the platform on down, in terms of
managing the containers, the runtime, and
isolation so that you have your own
space within the platform. Whereas, if you
are adopting and migrating workloads to
the cloud, and you're using
infrastructure as a service, then the
cloud provider manages hypervisor on
down. If you are using virtual servers or
if you are using bare metal, then you can
completely control everything on up, from
the operating system, the virtual servers
that you run, and the data you bring it
on. So it's very important to understand
the adoption model, whether you're
consuming Iaas, or PaaS, or if you're
consuming SaaS -
where the club provider manages all the
applications, and the security of it.
You worry about the data that you bring
in, and plan accordingly. So that's a very
important thing, because it's part of
understanding your responsibility in
ultimately managing the risk and
compliance of the workloads and the data
that you bring to cloud. Now let's talk
about architecture. When you build
applications and migrate applications, or
modernize your apps - let's start with
data with all the risk that you deal
with. And the kind of data matters. Is it
confidential data? Is it public data or
sensitive data, that may deal with
private information? Consider all those
factors and make a secure design around
what your data security architecture
should be. Make sure you have data at
rest encryption so that the data is
always encrypted, whether you use a
database as a service, object store as a
service, or other ways to store data like
block storage. Encryption is for amateurs.
If you think about key management, is for
professionals. So, having more control of
your keys, provide you the ability, in the
context of shared responsibility model,
that you own your data. You have complete
control of your data. As you think
about key management, make sure you have
an approach to think about if you are
bringing confidential data - you want to
bring your own keys. Maybe sensitive data,
you want to keep your own keys, so that
how much control of the keys you have
and the hardware security module in
which the key processing the encryption/
decryption operations happen. More
control you have, more responsibility
that you can take on. So encryption at:
data at rest,
data in motion - as it comes from services
to data stores or applications, so that
as you think about data coming all
the way. Your request and API requests
coming all the way - data in motion.
And in the new world you need to start
thinking about when the application is
actually processing the data, that is
going to be data in this memory. So you
can actually start to protect data using
hardware based technologies where you
can protect in-memory data as well. So
that when it is in use, and in memory by
the applications, you can protect it.
Take a holistic approach to data
protection at rest, in motion, in use, with
full control of your keys. It can be
bring your own keys, or even better, push
the boundary with keep your own keys. The
application that serves the data - it's
not only about which application needs
to have access. Make sure the data access
is only on need by need basis. Do not
open up your data services to the whole
world, be it network access, or everybody to
access the data. Make sure you exactly
know which applications need to access,
or which users need to access the data
to run your cloud applications. From an
application viewpoint, make sure there
are no vulnerabilities in your
application. So scan your applications.
Have an AppSec application security
approach so that you can do dynamic
scanning or static scanning of your
application before you deploy it into
the production. In the cloud native
environment, you are deploying container
images. So you can scan your images. You
can scan it for vulnerabilities before
you deploy, and set your policies so that
you only have secured images in
production any time. If there is any
vulnerability in the new world, you don't
need to patch these systems, you just
spin up a new container and off you go.
That's the beauty of a cloud native
approach; that you have security built in
in every step. At a container level
and the applications that serves the
business logic, you can start to
protect them. Then when you look at the
users coming in, you want to manage
access in terms of who the user is, and
from where they are coming from. So,
identity - you need to make sure who the
user is,
or which service it is, based on the
identity of those services or users, so
that you can maintain access control to your
application or data. And also from the
perspective of network access, you want
to make sure only authorized users can
get in. If there are intruders out
there, you can make sure you set it
up so that they are prevented from
accessing your application and your data
in the cloud - be it through web application
firewalling, network access control, or
distributed denial of
service protection, and have intelligence
built into these network protections as
well. So both identity and network - in
essence, you are protecting your data. You
need to manage access to your apps and
the workload on the data that you have
deployed on the cloud. In the next video,
we will look at security monitoring and
DevOps security.
