INTRO
-----


Give an introduction to Software Architecture. What it is, when is useful. Practices. Looking at code in a global sense. General overview of the example (a microblogging tool similar to Twitter) Security aspects of architecture.


Software Architecture
----

At its essence, software development is about managing complex systems.

In the early days of computing, programs where relatively simple. Perhaps calculate a parabolic trajectory or factorise numbers. The very first computer program, designed in 1843 by Ada Lovelace, calculated a sequence of Bernoulli numbers. As the posibilities of the new invention started to be explored, more and more complex operations and systems where designed. Tools like compilers and high-level languages multiplied the posibilities and the rapid advancement of hardware allowed to perform more and more operations. This quickly created the need to manage all the complexity and apply consistent engineering principles to the creation of software.

After more than 50 years of the birth of the computing industry, the tools at our disposal are incredibly numerous, and we stand over the shoulders of giants to build our own software. We can add quickly a lot of functionalities with a relative small effort, either leveraging high-level languages and APIs or using out-of-the-box modules and packages. But this great power comes with the great responsability of keeping care of the inherent growing of complexity that it produces.

In the most simplified way, Software Architecture defines the structure of a software system. This architecture can develop organically, usually at the early stages of projects, but after some growth and changes, the need to apply careful thought to it becomes more and more important. As the system becomes bigger, the structure becomes more difficult to change, which shapes the future effort. Making changes following the structure becomes easier than against the structure.

    Making certain changes difficult to do is not necesarely always a bad thing. That could involve elements that require to be overseen by different teams, or perhaps elements that can have effect in external customers. While the main focus is to create a system that's easy and efficient to change in the future, a smart architectural design will decide the proper balance of the parts based on the requirements.

The Software Architecture of a system is, then, looking at the bigger picture and necesarely at the long term, trying to help the day-to-day operations without being dragged too much by then. The usual choice between short term wins and long term operation is very important in development, creating the technical debt. Software Architecture deals mostly with the long term implications.

The requisites for the software architecture can be quite numerous, and could require balancing between them. Some examples may include:

- ** Business vision **, if the system is going to be commercially exploited. This may include requirements coming from stakeholders like marketing, sales or management. 
- ** Technical requirements **, like being sure that the system is scalable and applicable to certain number of users, or that's fast enough for the application. A news website require a different update time than a real-time trading system.
- ** Security and reliability concerns **, which can be more relaxed or less, depending on how risky or critical the application is.
- ** Division of tasks **, to allow multiple teams, perhaps specialised in different areas, to work fluidly at the same time in the same system. 
As systems grow, the need to divide them into semi-autonomous, more smaller components, gets more pressing. Small projects may live long with a "single-block" or monolith approach.
- Others

All this requisites, and others may influence the structure design of the system. In a sense, the Software Architect is responsible to implement the application vision, meaning what and how the system should do what it does, and match it with the specific technologies and teams that will develop it. That makes the Software Architect an intermediate lynchpin between both the business teams and the technology teams, as well as between the different technology teams. Communication is a critical aspect of the job.

To enable that successful communication, a good architecture should define boundaries between the different aspects and assign clear responsabilities. The Software Architect should, in addition to define clear boundaries, facilitate the creation of interface channels between the elements, and follow up on the implementation.

Ideally, the architectural design should happen at the start of the system, with a well thought design based on the requirements for the project. This is the general approach in this book, because it's the best way to explain the different options and techniques, but it's not the most common use case in real life. The challenge of a Software Architect is mainly to work with running systems that need to be adapted, making incremental approaches towards a better system, all while not interrupting the normal daily operation.


Dividing into smaller units
---

The main technique for Software Architecture is to divide the whole system into smaller elements, and describe how they interact with each other. Each smaller element, or unit, should have a clear function.

For example, some common architectures of typical systems can be a web service, composed of:

- A Database that stores all the data, in MySQL
- A web worker that serves dynamic HTML content, written in PHP
- An Apache web server that handles all the web requests, returns any static files like CSS and images, and forwards the dynamic requests to the web worker.

    This architecture and tech stack has been extremely popular since the early 2000s and was called LAMP, due the acronym for the different open source projects involved: (L)inux as an operating system, (A)pache (M)ySQL and (P)HP. Nowadays, the different technologies can be swapped for equivalent ones, like using PostgreSQL instead of MySQL or Nginx instead of Apache, but still sometimes keeping using the LAMP name.

As you can see, each different element has a distinct function in the system. They interact with each other in clearly defined ways. This is known as **Single-responsability principle**. When presented with new features, most use cases will fall clearly within one of the elements. Any style changes will be handled by the web server, and dynamic changes to the web worker. There's dependencies between the elements, as the data stored into the database may need to be changed to support dynamic requests, but they can be detected early in the process.

    We will describe in greater detail this architecture in Chapter TBD

Each element has also different requisites and characteristics. 

- The Database requires to be reliant, as it stores all the data. Maintenance work like backups and recovery from there will be important, and it won't be updated very frequently, as databases are very stable. Changes in the table schemas will be done through restarts in the web worker.
- The web worker requires to be scalable, and not store any information. Instead, any data will be sent and received from the database. This element will be updated often.
- The web server will require some changes for new styling, but won't happen very often. Once the configuration is properly set up, this element will remain quite stable.

As we can see, the work balance between elements is very different, as the web worker will be the focus for new work, and the other two elements will be much more stable. The database will require specific work to be sure that's in good shape, as it's arguably the most critical element of the three. The other two can recover quickly if there's a problem, but a corruption in the database will generate a lot of problems.

The communication protocols are also different. The web worker talks to the database using SQL statements. The web server talks to the web worker using a dedicated interface, normally FastCGI or similar protocol. The web server communicates with the external requests in HTTP requests. The web server and the database doesn't talk to each other.

These three protocols are different, which doesn't have to be the case for all systems, where different components may share the same protocol. For example, a RESTful interface.

# In-process communication

The typical way of looking at different units is as different processes running independently, but that's reductionist. Two different modules inside the same process can still follow the Single-responsability principle.

    The single-responsability principle can be applied at different levels, and is used as well to define the division between functions or other blocks. So it can be applied in smaller and smaller scopes. It's turtles all way down! But, from the point of view of architecture, only the higher level elements are important. Knowing how far to go on detail is clearly important, but when taking an architectural approach, is better to err on the "Big Picture" side than to the "Too much detail" one.

A clear example of this is a library that's maintained independently, but it could be also certain modules. The important characteristic is that the API need to be clearly defined and the responsability well defined to make sense to create an independent element.

    Creating a big component with internal divisions only is a well known pattern called a Monolith. The LAMP architecture described above is an example of that, as most of the code is defined inside the web worker. Monoliths are the usual de-facto start of projects, as normally at the start there's no big plan ahead, and dividing strictly into multiple components doesn't have a big advantage when the code base is small. As the code base and system grows more and more complex, the division of elements inside the Monolith starts to make sense, and later it may start to make sense to split it into several components. We will discuss more about Monoliths in chapter TBD

Inside the same process, communication is typically straight-forward, as it will use internal APIs. In the vast majority of cases, the same language will be used.


Conway's Law effects on Software Architecture
---

A critical concept to always keep in mind while dealing with architectural designs is Conway's Law. Conway's Law is a well known adage that describes that the systems introduced in organisations mirror the communications pattern of the organisation structure (https://www.thoughtworks.com/insights/articles/demystifying-conways-law)

This means that the people's structure is replicated, either explicitly or not, into the software created by an organisation. In a very simplifyed way, a company that has two big departments, purchases and sales, will tend to create two big systems, one focused in buying and another in selling, that talk to each other, instead of other possible structures, like a division by product.

This can feel natural, after all, communication between teams is different than within the teams. The first one will be more structured, and will require more active work. The communication inside a single group will be more fluid and less rigid. These elements are key for the design of a good Software Architecture. 

The main implication for the successful application of any Software Architecture is that the team structure needs to follow quite closely the designed architecture. Trying to deviate too much will result difficult, as the tendency will be to structure, de-facto, everything, following the group divisions. In the same way, changing the architecture of a system will likely result in restructuring the team organisation. This is a difficult and painful process, as anyone that has experienced a company reorg can describe.

Responsability division is also a key aspect. A single software element should have a clear owner and this shouldn't be distributed across different teams, as they will have different goals and focus, which will complicate long-term vision and create tensions. The reverse, a single team taking ownership of multiple elements is definetively possible, but require also some evaluation to ensure that this doesn't overstress the team. If there's a big missmatch between elements and teams (e.g. many elements per team), is likely that there's a problem with the Architecture of the system.

As remote work becomes more common and teams are located in different parts of the world, communication also results impacted. That's why it has been very common to set up different branches that take care of different element of the system, and using the need to create detailed APIs to line up with the physical barriers of geographical distance. Communication improvements also have an effect in the capacities for colaboration, making remote work more effective and allowing full remote teams to work closely in the same team.

    The recent COVID-19 crisis has increased greatly the trend for remote workers, specially in software. This is resulting in more people used to work remotely with other team members and in better tools adapted to work in this way. While timezone differences are still a big barrier to communication, more and more companies and teams are learning to work effectively in full-remote mode. Remember that Conway's Law is very dependent on the communication dependencies of organisations, but the communication itself can change and improve.

Conway's Law should not be considered an impediment to overcome, but a reflection that the organisational structure has an impact in the structure of the software. Software Architecture is tightly related to how different teams are coordinated and resposabilities are divided. It has an important human communication component.

Keeping this in ming will help design a successful Software Architecture so the communication flow is fluid at all times, and identifies problems in advance. Software Architecture is very related to human aspects of the work, as the architecture will ultimately be implemented and maintaned by engineers.


General overview of the example
----
During the whole book, we will be using an application as example to the different elements and patterns presented. This application will be simple, but divided into different elements for demonstration purpuses. The full code for the example is available in GitHub (TODO), and parts of it will be presented in the different chapters. The example is written in Python, using common frameworks and modules.

The example application is a web application for microblogging, very similar to Twitter. In essence, users can write small text messages that will be available for others users to read.

The architecture of the example can be described this way:

GRAPH


It has the following functional high-level elements:

- A public web site in HTML that can be accessed. This includes information for login, logout, write new microposts and read other users microposts (no need to be logged for this)
- A public RESTful API, to allow the usage of other clients (mobile, JavaScript, etc) instead of the HTML site. It will authenticate the users using OAuth, and perform actions similar to the web site.
- A task manager that will execute event-driven tasks. We will add periodic tasks that will calculate daily statistics, as well as sending an email notifications to users when named in a micropost.
- A database that stores all the information. Note that it's access shared between the different elements
- Internally, a common package to ensure that the DB is accessed correctly for all the services. This package works as a different element.


Security aspects of architecture
----

An important element to take into consideration when creating an architecture are the security requirements. Not every application is the same, so some can be more relaxed in this aspect than others. It's not the same an internet forum about cats than a banking application.

The most common example of this is the storage of passwords. The most naive approach about passwords is to store them, in plain text, near the username or email. When the user tries to log, we receive the input password, compare with the one stored previously and, if they are the same, allow the user to log. Right?

Well, this is a very bad idea, because that can produce serious problems:

- If any attacker had access to the storage on the application, they'll be able to read the passwords of all the users. Users tend to reuse passwords (even if it's a bad idea), so, paired with their emails, they'll be exposed to attacks on multiple applications, not only this one.
  This may seem unlikely, but keep in mind that any copy of the data is susceptible, including backups.
- Another real possibility are inside workers that may have legitimate access to the system, but that they copy the data for bad purposes. For very sensible data, this can be a very important consideration.
- Mistakes like displaying the password of the user on status logs.

To do so, the data needs to be structured in a way that's as safe as possible to access or even copy, without exposing the real passwords of the user. The usual answer to that is to have the following schema:

- The password is not stored. Instead, a *cryptographical hash* of the password is stored. This applies a mathematical function to the password and generates a replicable sequence of bits, but the reverse operation (from the hash discovering the password) is incredibly difficult.
- As the hash is deterministic based on the input, a malicious actor could detect duplicated passwords, as their hashes are the same. To avoid this problem, a random sequence of characters, called a *salt* is added for each account. This will be added to each password before hashing, making two users with the same password, but different salts, to store different hashes.
- Both the resulting hash and salt are stored.
- When a user tries to log, their input password is added to the salt, and the result compared with the stored hash. If it's correct, the user is logged.

Note that the actual password is unknown to the system. It's not stored anywhere, and only accepted temporarely to compare it with the expected hash, after being processed. 

    This example is presented in a simplified way. There are multiple ways of using this schema, and different ways of comparing a hash. For example, the `bcrypt` function can be applied multiple times, increasing over time, which can increase the time required to produce the valid hash, making it more resistant to brute force attacks.

This kind of system is more secure than one that stores the password directly, as the password is not known by the people operating the system. 

  The third problem described above may still happen! Extra care should be taken to be sure that sensible information is not being logged by mistake.

In certain cases, the same approach can be taken to encrypt data stored, so only the customers can access their own data. For example, enabling end-to-end encryption for a communication channel.

While this book won't cover in details aspects of security, it has a close relationship with the Architecture of a system. As we saw before, the Architecture define the aspects that are easy and difficult to change, and can enable making some unsafe things impossible to do, like knowing the password of a user, as we described in the example. Other alternatives are not storing data from the user to keep privacy, or reduce the data exposed in internal APIs, for example. Keep in mind that Software security is very difficult problem, and an approach to make operations unconvenient could help to make more difficult data leaks.
