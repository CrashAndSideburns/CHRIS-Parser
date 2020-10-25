Classes
=======

chris-parser uses a variety of classes to store data, enabling a maximum of
versatility once a .chris file is parsed, and allowing you to access all of the
fields of a parsed .chris file as attributes thereof.

Chris
-----

This is the base class output by the parse function, and all parsed .chris files
are members of this class. The Chris class is very simple, having no methods
and only four attributes. As a data class, all instances of Chris are immutable.

quote
^^^^^

All instances of Chris will have an associated quote, which is a string
containing the quote stored in the .chris file which was parsed.

author
^^^^^^

All instances of Chris will have an associated author, which is an instance of
Author containing information about the author stored in the .chris file which
was parsed.

date
^^^^

A date is not mandatory for a .chris file to be valid, so all instances of Chris
will have either None if the parsed file contained no date info or an instance
of Date containing information about the date stored in the .chris file which
was parsed.

context
^^^^^^^

A context is not mandatory for a .chris file to be valid, so all instances of
Chris will have either None if the parsed file contained no context info or a
string containing information about the context stored in the .chris file which
was parsed.

Author
------

This is one of the two base classes required to instantiate Chris, and contains
the author of the quote in a parsed .chris file. The Author class is very
simple, having no methods and only two attributes. As a data class, all
instances of Author are immutable.

last_name
^^^^^^^^^

All instances of Author will have an associated last_name, which is a string
containing the last name of the author of a .chris file.

first_name
^^^^^^^^^^

All instances of Author will have an associated first_name, which is a string
containing the first name of the author of a .chris file.

Date
----

This is one of the two base classes required to instantiate Chris, and contains
the date of the quote in a parsed .chris file. The Date class is very simple,
having no methods and only three attributes. As a data class, all instances of
Date are immutable.

year
^^^^

All instances of Date will have an associated year, which is a string
containing the year of the quote stored in a .chris file.

month
^^^^^

All instances of Date will have an associated month, which is a string
containing the month of the quote stored in a .chris file.

day
^^^

All instances of Date will have an associated day, which is a string
containing the date of the quote stored in a .chris file.
