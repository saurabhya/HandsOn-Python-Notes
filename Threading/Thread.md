# What is a Thread?

---
A thread is a separate flow of execution. This means that your program will have two things happening at once. But for most Python3 implemenations the different threads do not actually execute at the same time: tthey merely appear to.

It's tempting to think to threading as having two (or more) different processors running on your program, each one during an independent task at the same time. That's almost right. The threads may be running on different processors, but they will only be running one at a time.

Getting multiple tasks running simultaneously requires a non-standard implementation of Python, writing some of your code ina different language, or using multiprocessing which comes with some extra overhead.

Because of the way CPython implementation of Python works, threading may not speed up all tasks. This is due to interactions with the GIL that essentially limit one Python thread to run a time.

Tasks that spend much of their time wasting for external events are generally good candidates for threading. Problems that require heavy CPU computations and spend litle time waiting for external events might not run faster at all.

This is true for code written in Python and running on the standard CPython implementations. If your threads are written in C they have the ability to release the GIL and run concurrently.
