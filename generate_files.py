#!/usr/bin/env python3
import base64

with open("index.html", "w") as f:
    f.write(
        """
<html>
<img src="green.png" width="600" height="400"/>
</html>
"""
    )

with open("green.png", "wb") as f:
    f.write(
        base64.b64decode(
            "iVBORw0KGgoAAAANSUhEUgAAAAoAAAAKCAYAAACNMs+9AAAAFUlEQVR42mNk+M9Qz0AEYBxVSF+FAAhKDveksOjmAAAAAElFTkSuQmCC"
        )
    )
