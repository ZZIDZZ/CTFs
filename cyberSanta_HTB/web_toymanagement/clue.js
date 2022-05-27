//http://178.128.46.48:30450/

//' = '''

async loginUser(user, pass) {
	return new Promise(async (resolve, reject) => {
		let stmt = `SELECT username FROM users WHERE username = '${user}' and password = '${pass}'`;
		this.connection.query(stmt, (err, result) => {
			if(err)
				reject(err)
			try {
				resolve(JSON.parse(JSON.stringify(result)))
			}
			catch (e) {
				reject(e)
			}
		})
	});
}

router.post('/api/login', async (req, res) => {
	const { username, password } = req.body;
	if (username && password) {
		passhash = crypto.createHash('md5').update(password).digest('hex');
		return db.loginUser(username, passhash)
			.then(user => {
				if (!user.length) return res.status(403).send(response('Invalid username or password!'));
				JWTHelper.sign({ username: user[0].username })
					.then(token => {
						res.cookie('session', token, { maxAge: 43200000 });
						res.send(response('User authenticated successfully!'));
					})
			})
			.catch(() => res.status(403).send(response('Invalid username or password!')));
	}
	return res.status(500).send(response('Missing parameters!'));
});