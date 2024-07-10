# taglit

This is similar to [what's being planned for a future PEP](https://github.com/jimbaker/tagstr/blob/main/pep.rst).
It uses some `ast` magic to automatically replace any **uppercase** f-strings (`F'...'`) with behavior similar to what's described in the PEP.

Here's an example:

```python
from taglit import taglit, html

def is_logged_in() -> bool:
    return False

animal_images = ["cat.png", "dog.png", "cow.png"]
status_image = "logged-in.png" if is_logged_in() else "logged-out.png"

@taglit(html)
def demo():
    return F'''
        <div>
            <img src={status_image}>
            <ul>
                {(F'<li><img src={image_file}></li>' for image_file in animal_images)}
            </ul>
        </div>
    '''

print(demo())
```

```html
<div>
    <img src='logged-out.png'>
    <ul>
        <li><img src='cat.png'></li><li><img src='dog.png'></li><li><img src='cow.png'></li>
    </ul>
</div>
```
