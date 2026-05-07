#!/usr/bin/env bash
    # exit on error
    set -o errexit

    # Install dependencies
    pip install -r requirements.txt

    # Convert static files (CSS/JS) for production
    python manage.py collectstatic --no-input

    # Apply database migrations
    python manage.py migrate
    ```

---

### 3. Make `build.sh` Executable (Very Important)
Render needs "permission" to run the script you just created. If you are on a Mac or Linux terminal, run this command:
```bash
chmod +x build.sh
