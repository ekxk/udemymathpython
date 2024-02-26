#pip install handcalcs

# first way
Equation 1
$$\frac{sin(x)}{x}$$

foo bar 

# second way
Equation 2
\begin{equation}
F(k) = \int_{-\infty}^{\infty} f(x) e^{2\pi i k} dx
\end{equation}

# third way
import handcalcs.render
%%render
a = 23
b = 43
c = 2
d = 3.226

f = d / a + b

# will have an output of latex code
# copy the latex code into the text cell.
