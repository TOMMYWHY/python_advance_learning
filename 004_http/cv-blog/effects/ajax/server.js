const http = require('http');
const fs = require('fs');
const url = require('url')
// const request = require('request')
const port = 9999

let sessions = {}

let server = http.createServer(function (req, res) {
    let parsedUrl = url.parse(req.url, true);
    let pathWithQuery = req.url;
    let queryString = "";
    if (pathWithQuery.indexOf('?') >= 0) {
        queryString = pathWithQuery
            .substring((pathWithQuery.indexOf('?')))
    }
    let path = parsedUrl.pathname;
    let query = parsedUrl.query;
    let method = req.method;

    /*=================*/

    console.log('query string is :' + pathWithQuery)
    if (path === '/') {
        let string = fs.readFileSync('./index.html', 'utf8')
        let cookies = '';
        if (req.headers.cookie) {
            cookies = req.headers.cookie.split(';')
        }
        let hash = {}
        for (let i = 0; i < cookies.length; i++) {
            let parts = cookies[i].split('=');
            let key = parts[0]
            let value = parts[1]
            hash[key] = value
        }
        console.log(hash);
        let mySession = sessions[hash.sessionId]
        let email;
        if (mySession) {
            email = mySession.signin_email
        }
        let users = fs.readFileSync('./db/users.json', 'utf-8')
        try {
            users = JSON.parse(users); //to object
        } catch (exception) {
            users = []
        }
        let foundUser;
        for (let i = 0; i < users.length; i++) {
            if (users[i].email === email) {
                foundUser = users[i];
                break;
            }
        }
        // console.log(foundUser.password);

        if (foundUser) {
            string = string.replace('__password__', foundUser.password)
        } else {
            string = string.replace('__password__', 'not login yet')
        }

        // console.log(string);

        res.statusCode = 200
        res.setHeader('Content-Type', 'text/html;ch1arset=utf-8');

        res.write(string)
        res.end()
    } else if (path === '/main.js') {
        res.statusCode = 200
        res.setHeader('Content-Type', 'text/javascript;charset=utf-8');
        let string = fs.readFileSync('./main.js', 'utf8')
        res.write(string)
        res.end()
    } else if (path === '/other.js') {
        res.statusCode = 200
        res.setHeader('Content-Type', 'text/javascript;charset=utf-8');
        res.setHeader('Cache-Control', 'max-age=30')
        let string = fs.readFileSync('./other.js', 'utf8')
        res.write(string)
        res.end()
    } else if (path === '/style.css') {
        res.statusCode = 200
        res.setHeader('Content-Type', 'text/css;charset=utf-8');
        let string = fs.readFileSync('./style.css', 'utf8')
        res.write(string)
        res.end()

    } else if (path === '/signin' && method === 'GET') {
        let string = fs.readFileSync('./signin.html', 'utf8')
        res.statusCode = 200
        res.setHeader('Content-Type', 'text/html;charset=utf-8');
        res.write(string)
        res.end()
    } else if (path === '/signin' && method === 'POST') {
        readBody(req).then((body) => {
            // console.log(body);
            let strings = body.split('&')
            let hash = {}
            strings.forEach((string, index) => {
                let parts = string.split('=')
                let key = parts[0]
                let value = parts[1]
                hash[key] = decodeURIComponent(value)
            })
            console.log(hash);
            let { email, password } = hash
            let users = fs.readFileSync('./db/users.json', 'utf-8')
            try {
                users = JSON.parse(users); //to object
            } catch (exception) {
                users = []
            }
            let found = false;
            for (let i = 0; i < users.length; i++) {
                let user = users[i];
                if (user.email === email && user.password === password) {
                    found = true;
                    break;
                }
            }
            if (found === true) {
                res.statusCode = 200
                let sessionId = Math.random() * 10000
                sessions[sessionId] = { signin_email: email }
                res.setHeader("Set-Cookie", `sessionId = ${sessionId};HttpOnly`)
            } else {
                res.statusCode = 401
            }
            res.end()
        })

    } else if (path === '/signup' && method === 'GET') {
        let string = fs.readFileSync('./signup.html', 'utf8')
        res.statusCode = 200
        res.setHeader('Content-Type', 'text/html;charset=utf-8');
        res.write(string)
        res.end()
    } else if (path === '/signup' && method === 'POST') {
        readBody(req).then((body) => {
            // console.log(body);
            let strings = body.split('&')
            let hash = {}
            strings.forEach((string, index) => {
                let parts = string.split('=')
                let key = parts[0]
                let value = parts[1]
                hash[key] = decodeURIComponent(value)
            })
            console.log(hash);
            let { email, password, password_confirmation } = hash
            if (email.indexOf('@') === -1) {
                res.statusCode = 400
                res.setHeader('Content-Type', 'application/json;charset=utf-8');

                res.write(`
                {
                    "errors":{
                        "email":"invalid"
                    }
                }
                `)
            } else if (password !== password_confirmation) {
                res.statusCode = 400
                res.write('passowrd not match~!')
            } else {
                let users = fs.readFileSync('./db/users.json', 'utf-8')

                try {
                    users = JSON.parse(users); //to object
                } catch (exception) {
                    users = []
                }
                let inUse = false
                for (let i = 0; i < users.length; i++) {
                    let user = users[i];
                    if (user.email === email) {
                        inUse = true;
                        break;
                    }
                }
                if (inUse === true) {
                    res.statusCode = 400
                    res.write(' email used ~!')
                } else {
                    users.push({ email: email, password: password })
                    let usersString = JSON.stringify(users); //to string
                    fs.writeFileSync('./db/users.json', usersString);
                    res.statusCode = 200
                }

            }
            res.end()
        })

    } else if (path === '/mvvm' && method === 'GET') {
        res.statusCode = 200
        res.setHeader("Content-Type", 'text/html;charset=utf-8')
        let string = fs.readFileSync('./mvvm.html')
        res.write(string)
        res.end()
    } else if (path === '/books/1' && method === 'GET') {
        readBody(req).then((body) => {
            console.log(body);
            res.statusCode = 200
            // res.setHeader('Content-Type: text/json; charset=utf-8')
            let data = {
                name: 'nonviolent communication',
                number: 2,
                id: 1
            }
            data = JSON.stringify(data)
            // res.send()
            res.end(data)
        })
    } else if (path === '/books/1' && method === 'PUT') {
        readBody(req).then((body) => {
            let data = JSON.parse(body)
            // console.log(data);

            res.statusCode = 200
            // res.setHeader('Content-Type: text/json; charset=utf-8')
            let result = {
                name: 'nonviolent communication',
                number: data.number,
                id: 1
            }
            result = JSON.stringify(result)
            // res.send()
            res.end(result)
        })


    } else if (path === '/xxx') {
        res.statusCode = 200
        res.setHeader('Content-Type', 'text/json;charset=utf-8');
        // let string = fs.readFileSync('./main.js','utf8')
        res.write(`
        {
            "note":{
                "to":"tommy",
                "from":"aws"
            }
        }
        `)
        res.end()
    } else {
        res.statusCode = 404
        res.setHeader('Content-Type', 'text/html;charset=utf-8');
        res.write('ops~! 404')
        res.end()
    }


})

function readBody(request) {
    return new Promise((resolve, reject) => {
        let body = [];
        request.on('data', (chunk) => {
            body.push(chunk);
        }).on('end', () => {
            body = Buffer.concat(body).toString();
            resolve(body)
        });
    });
}

server.listen(port)
console.log('listening port :' + port + "   now...")

