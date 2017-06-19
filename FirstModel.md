

## PARSEL_INTERACTIVE

### USAGE

```python
import parsel, os
from urllib.request import urlopen

# Read sample HTML file
path = os.path.realpath('./scrapy.html')
htmlsample = urlopen('file://' + path).read().decode('utf-8')

doc = parsel.Selector(text=htmlsample)

# Selectors for nav-bar items
selector_list = doc.css('.navigation li')
```

```python
from parsel_interactive import interactive

obj = interactive()

# Highlight selectors and view HTML in browser
obj.show(selector_list, htmlsample)

# Make modifications to your selector and run
obj.show(modified_selector_list, htmlsample)

```

![Parsel-interactive](https://github.com/harshasrinivas/parsel-interactive/blob/master/images/1.png)


### Issues with Parsel-Interactive

Currently, for demonstration the model uses a saved HTML file. As you can see from the output, CSS is not loaded.
For the case where we need to obtain HTML from URLs, loading CSS files is an issue. So we need to obtain all the static CSS/JS files to visualize the website in a beautiful manner.

Possible solutions I have been experimenting with over the past few days:

* Using wget to obtain all static files of the website

> This solution involves an additional dependency (wget) 

* Changing the HREF attributes to loaded css files - from relative to absolute

> Ideal solution that can be made perfect




## SELENIUM-INTERACTIVE (For demonstration)

This is the desired way for this project to work. This method makes use of Selenium to show the desired working.

```python
from selenium_interactive import interactive

obj = interactive()

# Opens up a web browser
obj.open('https://scrapy.org/')

# Highlight selection using CSS selectors
obj.check_css('.navigation li')

# Clear the highlighted elements
obj.clear()

# Highlight selection using XPath
obj.check_xpath('/html/body/div/div')
obj.clear()

```

![Selenium-interactive](https://github.com/harshasrinivas/parsel-interactive/blob/master/images/2.png)
