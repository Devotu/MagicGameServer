PORTABLE KANBAN README.TXT

1. How to migrate database from version 2.x?

Version 3.x uses JSON-based format for data file. You can't directly use data from 
previos version and will have to import tasks using CSV file:

1) Export data in CSV format from PK 2.x.
2) Open in Excel.
3) Insert 2 empty columns between "Completed" and "Link". No need to type anything,
   these columns are reserved for "Canceled" and "Estimate" values.
4) Save as CSV file (not just Save!), then close Excel without re-saving file.
5) Open CSV file in PK: Setup/Import...

Preview records, if everything is Ok click on "Import". Add views, colors to topics,
tags, views etc.
Note: only 50 subtasks will be imported.

2. How to create shared kanban board?

Data file is strictly for personal use. Period.
If you need shared board install Redis database server.
Redis is free & open source multiplatform NoSQL server.
More about Redis: http://redis.io/
Version for Windows: https://github.com/MSOpenTech/redis
Short book: http://openmymind.net/2012/1/23/The-Little-Redis-Book/ (included)

Note: PK includes simple user management. You can assign different roles
to users - see Setup/Users. There is only one user by default - Administrator 
with a blank password. A good idea is to rename Administrator and set some
reasonably long password. If you lose it there is NO SIMPLE WAY to reset it. 

3. How to install Redis on Windows?

See links above. 
If you're just going to try shared board then you do not have to install
Redis server, there is simpler way: expand Server/redisbin.zip somewhere
and start redis-server.exe, server will run until you close its window.
Alternatively you can try cloud based Redis hosting services: 
http://duckduckgo.com/?q=redis+hosting.

4. I need feature XYZ, but there is no such one!

1) Please, keep in mind that PK is a very minimalistic tool.
2) Look into options (Setup/Options) and shortcuts (About/Shortcuts),
   maybe it's already there.
3) Consider workarounds, e.g. add more views and tags.
4) Vote for new features on http://dmitryivanov.net/personal-kanban-app/.
5) Consider donation if you need this feature a.s.a.p. It can be implemented as 
   a plugin or new built-in feature. Contact me by e-mail (About/Send e-mail
   within the program).
