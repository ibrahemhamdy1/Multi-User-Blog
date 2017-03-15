from google.appengine.ext import db

from user import User
"here  we  add  the  like  to  our  data stor"

class Like(db.Model):
    user_id = db.IntegerProperty(required=True)
    post_id = db.IntegerProperty(required=True)

    def getUserName(self):
        user = User.by_id(self.user_id)
        return user.name
