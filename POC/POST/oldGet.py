
	def GET(self):
		web.header("Content-Type","text/html; charset=utf-8")
		return """<html><head></head><body>
<form method="POST" enctype="multipart/form-data" action="">
<input type="file" name="thefile" />
<br/>
<input type="submit" />
</form>
</body></html>"""