# Ethan's Writeup :) 

### DLA Project

This coding project was implemented to study Diffusion Limited Aggregation (DLA) by introducing particles and sticking them together. This can help us understand phenomenons like Brownian motion and can help us probe fractal dimensionality. 

My program uses an iterative creation-circle to spawn new particles surrounding a central particle on a graph. The actual architecture of the program is as follows:
1. Creates an empty array for our aggregate to grow on.
2. Checks if the aggregate is full. If it's not, a new particle will keep spawning on a radius surrounding the middle.
3. The particle will move until it sticks to another particle by continually checking adjacent locations, moving, checking locations, moving, and repeating until the particle either gets stuck or goes into the death zone.
4. The death zone is about 20 units away from the spawning radius. If a particle crosses it, that particle is just deleted.
5. Once stuck, its distance from the middle is measured. The maximum distance away from the origin is incremented if needed as well, and if it is, then the spawning radius is incremented by that amount as well.
6. The Hausdorff dimension is calculated from the number of particles and maximum distance. A picture is drawn.

<figure>
  <img src=pictures/50000particles.png>
  <figcaption>Largest aggregate made, taking 1.5 hours to compute 50,000 particles. No stickiness factor.</figcaption>
</figure>
<p>&nbsp;</p> 

> [!NOTE] I think I severely underestimated the time it would take to finish this project and will not make that mistake on any more projects. I also had a lot of problems with my program, which eventually ended with me re-writing my entire program in one weekend (which was obviously not ideal). Due to time constraints and poor time management, I did not end up implementing a stickiness factor. If I had implemented a stickiness factor, I could have gone into much more detail on fractal dimensionality. The architecture of the nested while and for loops was the most time consuming part of the code, as well as just generally tweaking small errors that kept piling up.

> [!NOTE] I also was not able to implement the stickiness factor. I know exactly how I would program it, but I did not have the time management organized enough to do so. :( 

### Specific Questions:

 1. What is the difference between capacity dimension and topological dimension?

Capacity dimension, also called Hausdorff dimension, is a way to describe a non-integer dimension of a fractal. Take, for example, the Cantor set. This sort of object cannot exist in any integer-dimensional space, since it has infinite points but also zero volume (I think). This is weird. So Hausdorff, or capacity dimensions, were invented to fix this. A capacity dimension is a way to describe how an object can be defined with smaller and smaller pieces within a certain area. 

Fractal dimension, also called topological dimension, is sort of a way to measure the circumference of the aggregate in a way that incorporates the aggregate's sides' roughness. 

The difference is that the Hausdorff dimension measures sort of how the shape behaves as a whole, whereas the fractal dimensionality is only concerned with the properties of the shape (like how rough it is on the edges).

 2. Can you replicate Witten and Sander's published capacity dimension?

To my understanding, Witten and Sander reported their capacity dimension to be 1.585. My aggregates, on average, ended up having a capacity dimension of around 1.72. I think this is a bit higher than theirs.

 3. How does the capacity dimension change as a function of *S*?

I don't know how to generate an explicit formula, but it seems as though as S increases, the capacity dimension decreases (but the fractal dimension increases). 

### Attribution:

The resources I used on this assignment were mainly just fellow students. Mateo taught me how to generate the images of the array and taught me how he incremented his spawn/death radii. My program's architecture was heavily influenced by his' as well. I tried to learn from Zeke but when he was explaining his code it was too ugly. Adam helped me understand conceptually what exactly capacity/fractal dimensionality is.

Some further resources I used were:

[1] https://en.wikipedia.org/wiki/Fractal_dimension

[2] https://en.wikipedia.org/wiki/Lebesgue_covering_dimension

[3] https://physics.weber.edu/schroeder/javacourse/DLA.pdf

[4] https://journals.aps.org/prl/abstract/10.1103/PhysRevLett.47.1400

[5] http://crossgroup.caltech.edu/Chaos_Course/Lesson9/Dimension.pdf

### Timekeeping:
The first version of my program, which ultimately failed, probably used about 8-10 hours of my time. The second, non-recursive final version of my program probably took around 20-30 hours over the course of 3 days (2/8 through 2/10 and the night of 2/12).

### Languages, Libraries, Lessons Learned:
 1. What language did you use for your program?

I used Python for the entire program. I stuck with it through the entire process, and I honestly learned alot about Python in the process and I like it (maybe a little more than C++ now).

 2. What libraries did you use in your submission? Were any of them remarkable? Great to use, super annoying to use, etc?

I used numpy, random, math, time, and matplotlib.pyplot. Numpy, random, math, and time were all really easy to use since they are seemingly so standardized. Matplotlib.pyplot took a bit of tweaking to figure out how to actually display my stuff.
