# coding: utf-8


from dictdiffer import diff, patch, swap, revert
import json

def main():
    first = {
        "title": "hello",
        "fork_count": 20,
        "stargazers": ["/users/20", "/users/30"],
        "settings": {
            "assignees": [100, 101, 201],
        }
    }

    second = {
        "title": "hellooo",
        "fork_count": 20,
        "stargazers": ["/users/20", "/users/30", "/users/40"],
        "settings": {
            "assignees": [100, 101, 202],
        }
    }

    # Calculate the diff
    result = diff(first, second)   # Return generator (yield)
    print(json.dumps(list(result))) 

    # Apply the diff like a patch
    patched = patch(result, first)
    print(json.dumps(patched))
    print(json.dumps(second))


if __name__ == "__main__":
    main()