from flask import Flask, jsonify, request

app = Flask(__name__)
"""
@app.route("/<route>", methods=["GET", "POST"])
def foo():
    pass
def test():
    data = jsonify(
    version = 1.0,
    value_list =[
        "abc",
        "def"
    ])
"""
@app.route("/", methods = ["GET"])
def main():
    return "Hello u wanna got response go to /skill"

@app.route("/test", methods=["GET", "POST"])
def test():
    data = jsonify(
    version = 1.0,
    value_list =[
        "abc",
        "def"
    ])
    return data

@app.route("/skill", methods=["POST"])
def skill():
    data = {
        "version": "2.0",
        "template": {
            "outputs": [
                {
                    "basicCard":{
                    "title": "카드의 제목",
                    "description": "상세 설명",
                    "thumbnail": {
                    "imageUrl": "data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQABAAD/2wCEAAkGBxMTEhUTExMVFRUXGBgYFxgYFxcXGBsYGh0YGBgVGBgYHSggGBolGxUXIjEiJykrLi4uFx8zODMtNygtLisBCgoKDg0OGxAQGy0lICUtLS0tLS0tLS0tLy0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLf/AABEIAKgBLAMBEQACEQEDEQH/xAAcAAACAwEBAQEAAAAAAAAAAAADBAECBQAHBgj/xAA/EAABAgQDBQUGBQMDBAMAAAABAhEAAwQhEjFBBVFhcYETIpGhsQYyUsHR8AcUI0LhYoLxFTNyJJKi0giD8v/EABsBAAIDAQEBAAAAAAAAAAAAAAIDAAEEBQYH/8QANhEAAgIBBAECBAUCBgIDAQAAAAECEQMEEiExQRNRBSJhcRQygaGx0fAjM0KRweEk8TRSYhX/2gAMAwEAAhEDEQA/APEFs9stIJpXwQuinUQ4SSN4EEsU5K0gXOKdNgiIWEREIdEIdEIdEIWQpsouMtrtEqwtLOwrCtxBh2nybMqkwJxuNGxtPaSCJnZjvTVYlncD+0DQZ+PCN+XNjhCSh3IzY8cnJOXgclhSClAJCESsayDY4snbRyI1RbhOMI9RXIqSu5PtukYlLSCZjOMJIcsRp9mOZi06yqUrqjXPJspUIkRjaocViiEvEIatB+osBg0tJwpORPHmc46GKXqNfLxFcL6+4jInFN+5etkmZiWVjupYH4yn3iG0uzweoxvLcr6X+9Awfp/LXZkKjms0jFHVFDs3eYXyzceYB6Q3Fk28LyDKNjU2RiQbhkuSo5qOoHB/ONE4b493Xn3ATp0Z2sYkN+5oImJUgBsayCGaydxHrzjWpRlGly/4FNNMz1pILHPKMrtOmN7NKYtSpVgwbJILW1JOvKNblKWPjr6CkkpCMhsQfLk/lrGbH+ZDJdDU9HfQz6fsbXQFnh2Tia/oBF/K/wCoPaCQCGfqnD8g/hFZ6tEx3RfZyFXKX0yY+KTnEwdMk+0LVEwqUScyeUKySuTYcUPUhUhDkBaDch8mte0aIbscOeYsVKpSpdmatTnWMsnbGrge2bLBOZC7YW6uW106PnGnTxTtdPwLyN9eANWtiQO7ooA2cZtwheTJfC4/qHFcCwhIRpUVMnvCYkuUgi9wNVDewu26NuDFG36nYjJN/wCkNWTUhC0L98MOBUkhljmkkHpDckouEovtf2mBBNyUvH98GTMmE5l7N0EYJzc3yakqBwsganl4lBO8gQzFDdNRBlLbFs+pqK4SCiUlCTiYFw7AkXTuPGPQZ834eWPFHzVnLxY3lUskmYm3pITNsMw/W8c34niUMtrpo26STlj5OkbFmKRjGFmBz39LQMPhuWcdy6JLVQjLazNWliRujDKO1tM0rlWQ0CQiIQ6IQl4hCQYtfQg/N2qtSMBNmAPEB2HmfExsnrJShtrkSsC3biUKCJB+KYpv7R/MEqxae/Mincsv0Q4JCUSygoBPZ41KOYJbCB4xojjxwx7ZLmrf38IS5Sc918XS/wCTNnUC0yxMUGSrL+d0YJ6acIKbNSyxctoo0I4DJCzviJtdFUaSarGlEsAJsApX9IJUelyTyjasu+Kx/wC/2QrZtbkVqpOMKmWGQSlrkPhfhkebGKyY/UTyL9CQe35TPMY+hw9SzCtkKUAhIdsnvl4mNOOTnUZdC5Lbyim0ZGFTgAA6DRrX6wOfGoy46LhK1yW2ZNY4fi4XfSL086ZWSNoptGWyrAdBYEZjid/OK1C5tF43xTC0QxJId20z6taDw/NFpsqfHIrLsscCN/yjPHiQbHKhIxoYWJ+E3vz70aMlb1x/IuL4YDaDOGGnwlP+YDPW7gKF0Gpkjsyrr8sxcQeNVAF9iSEuoDeYzRVyGPo0K+eAkJBzz0LCwChyP3rry5KhtQuK5EaSTiUAz72zbVuMZccd0qDk6RobRYIDu7DAq2Qs33w4xrzVGNeULgmZbvGNu+WOHaGnDgrDhThN2OINbgfqI04cUeHPp9fcXOTqol6lRQQHIWgjCrIlJuH4h/MweSWx3zcf3QMVa+jEZ80qJJzMZJzc3uY1KlQMQBYXsFfCb5WMMWGbVpMFyiE2etpiSd4hmlaWWJWVXBo+mrKALqpS3AlYUrKvhKScSSPixMw1BEdfNiyZNXF1wjBjnGGBxvkwtuzwqaWyH384w/Ecm/MadJBwxqxvYyiJU1RJaw4Wv840/D79Kc2/sJ1KTyRikZdBT9pMCN5vy1jm6fE82VR9zXlyenByNisopCkKEt8cv3t3QvfwEdTLpsMlKMFzEyQy5FJOXTMSnpVLLJSTHIx4Z5L2o2znGPbKTJZBYgg7oCUXF01yWmn0UaKLIiiEvEIWCou3Ra7NSZtPtAlBAAJRjNrhIwjoBHQ/FxnUa7q2ZlicU37dDlWgKWUFTgqUtTaS0OEjwv1jRkW6W2T7bb+y6Exe2Nr7fqxKoosa+4kI7iSQSwBIdnOp3RmyaffJbF4t/wBB0cm1fN7mU0c80EgxaddE7NGVWFWEFhgAwgZlQYJ++e+Nkcu+vp+7E7NtlK+mYgB1KYlX1A0H+YDNjXFd+QoSE0KILjMRnTcWHVmn2napw+N81bzwD+gjZu9WNCq2szVBjGLmLod2hycApDgZNe3hmwHDP56Z/NBMWuGCoD3iHsRC8P5qLmCnhlnn98IqaqYSdobqAMaGGu7lwL+fKHTdtALpi9f72TWELz/mLh0FnhpY3lvrzg8lRgio8yK7PlkkkaD752gMK5svJ7AaqY6n6QGV2y4qkOU0vCl8jnoWGhG/iIfiWyNsGXLE6icVEktfdlzhGSTk+Q4xpFqeQSCoAd1iRr4a5QWPHJrcvBUpJcDtWtLYgzLcsM0qDMW0zY8jwjRllHba6YuK55M6bNKi5LneYyTm5u2NSS6KJDwKV8Fs0KPZ4UFBRKVAgANqXbE+Qt5xsw6dSTUu/AmeWmq6NOUqoUlJlNhwgEEpsoWIueD9Y6MHqHFem0l9fczOOK/mPmwY4SddG8cTtOYAzxsj8QzRjtsS8EG7oVKnjI5OTtjjTl1IFOUAhybjW5b0jqQzQho3FPlmWUG824v7MYe3AUWcEPudrwv4Y1HNf0ZNZG8dDYkGVKnqXZSlqSBrYlzbR7cY0YG4Yssp+WLnU8kIx6SA0k5UmmC0FlrUwIzDbvvWBxN4dLuXcmXOKyZ2n0kB24kdsHtYYvnC/iKj60U/bkPTN7OAO06SWhKChROIPdvpCtXgx4oxcX2FhySm2muhQ0ysOLCcO9rRk9Ge3dTofvjdWBIhZZ0QhzxdkGaSsKFYmdwUkHUGxHhDsWdwk5Pm1QE4KSo0JVakoUtSv1CpSm3qIASeQdR8I2QzrY5t83Yl43uSBopsfZy7Bk4lKa/ePdHE3HjAekp1D6Wwt+25CE2QU3Ys5AOhbdGSeNx58DYyTBoUxcQu6dhNGlQTwXCj3lZqJthAdn+9N0bME1K93bFTXsBr6Zu8LDUMzaDO97wvPjp2i4S4oXp5rFtDY8ecKhLb0FJWNV0oHvDr8iePpaHZ4p00DGXgpQTTdL8fr5QOGXguarkCBhXyMB+WZfaL1g7z8PT7EXm7sqHQRRuj+OEE2uCAagd5uXygclOZa4ResVkHi8r8FQCDuS+J5a/x9iDXy47K7YvTS8RvkLmFY4uUgpNINtCeCwHM8/kYZmn4QMEBp5JUfttWHVmhWODkw26NSZUJlpBTf4dbPdJPn4cX2vJGEeBKi2+TGUY57lb5HlpUrEW4gcL2vBQg5NIpujUl7PASpLOsF0qD7iR0OFQ5iNywKMXffgQ8luwf5oJUF5haRiG5Q1HFwCOcU8ihkU5dPv7l7LjS8Ck6qJUohwFKJYcTGXJlbk3F0hiiq5FYSGdEITEIc8WQtKmFJcFiIKE3CW5dlSSkqYeprVrso2h+fWZMyqQGPFGD4NLZ20ZfZJlzA+BYWl3zD2tmC4cf0jjGrT5MU8ahkfTsTkxyUm4+TPrqgzZil6k8vIZRkz5PXyX78DscfThQztdjMQgZBKU+Oca9cryxxr2SFae1ByfuzSrphaeguES0pSE6Yjrzb0jXmmmpx/0qNfqZ8ceYvy2xIUMsS2L9pg7R9AN33xjKtLBY9vmrsb60pTtdXQj/AKevs+1th89ztueMX4afp+p4NHqx3bRUphAwiKIS8WWO020CkLs5U1zoQ7Hz8hGnFnau+3X7CpY069hqdNSSye8lKTmLOQEpSPI83jROUW6XNARVcsTqqPDkXYB9LkkMN4tGXLh2q17chxnYrlCfysYP09S74rqOpvnYnoMo0wybuxco+wCtpikvofLh/MLy49rsKMrCUU0MUn74QWGSqmDJeQCxgV5iFP5JWF2i9Xdj97/rBZeeUSPsAXMeAcrLopAlmorZShJTPBBB01DRaZBB8Sou9zK6QWrmOW0g8jukioqg8tfZp4/P+IYnsiA1uYlKQVFoQluYxujRWoSxvBDEb99/MczGqTWNClcmZkxZJeMkm2xyDU1OVcA7PxZwIPHj3fYGTofKAEAjuhaWN7YhcHxChGylGNx/ti7t0Cm7TPdKO6piFcXL+rnrC56nbW0ixe5nFUY2xxESyERRDohDohDohDohDohCXiEJBi066IXM4lWIlzv5QbyyctzfJVKqH67axmJw5OQVcSAEgnfYCNWbVqcdsVV9iceHa919dDdbWyzLJT760IQ3w4fe8bZ8Y0ZMsdrkny0lQrHiaaTXCthK6XhQS4ZSJSEXzdlKPQhjDMv5GvDSSBgvmS+rbAbWSAjAwARMwC17J7543MK1Lh6dVwml/UPDu3W/K/8AQrM2fimFEvQAkqYNYOD1LRmnp7ybYew1ZajchFUojTVuu6Mzg1z4HJplGgCBJc0ggjQg+GUHGbiU0PU1YCoqWb3V1DBIHIP1aNMMyvkW4EronSD+4947u8zDhmbxHguNkWSnRnlJB3GMrTixvY9TTsXdVfhof5zvxMaYSU1UhclXKFZ8opNstPvfCJx2vgKLtF5isYfUff8AMHJ7kRcA8bpbjC7+WmSubKdmWdvvJ+IeBCOlSlKICUlRNgAHJO4AZxCDlXKnoATMC0M3dUCkgHIlJYsd+UQgrJUAb8YKDplSVotKDnEecFBW7KbpUdNWVG3SKlJydESobRhlp4+Z4cv4h8axxA5kxBayo3++EZpScmMSobpKN/e8NdWPiGaNGHDb5AnP2DTpyUFQGSg7DRVx0uAekMlNQ48FU5CE2cVPud20eMksjfHjsZSBQJZaXKJIAFyWEWot1RTaXYZdIpJKVWILEWgp43B1LspSTVoAiWTYAnkHgYxlLpFtpdnKSRmCIpxcXTRE0+iGiizmiEOaIQiIQ6IQ6IQ6IQmIQkGL7IEM5RZzllDfWk63ProHahmqr1TFJx5D7J5w2eo9WS3dAxx7UxqjqUlUxai3eCgN4GIt44Y0YsqlKU/r+yFThSjEtPB7OWmxxFBA3kuVHxIESUrhFe9cfuyRS3N+1gJ9KkhaxbvskDJnAPrbkYXPCpbpr9P96DjNppMTn0qkuWcBWF9H3RllicRkZWBELCGJFWpNtP4Z/CGwzNAOKY0AlYYaDqMgOeghy2zQPMRKbKKb6aGM8oSgGmmFTNxBj98ecGpqSoqq5BB0mAva6L7Q3smlTMqZMtRZMybLSeSlJB8jFTJFnqW16iirZW0aP8umTNo0TVU8wLViV2CglQUGwgqNgBniaxDwDdBIzPw9p5FJQ11dPkdrOkdl2aFY0WmEIBILHDiUHO4QMZxl07LpjvtLtKVtPY02q7JMqdRzJYOB8JTNUlGFOJ1DO4cjug8ARR5HFkCqUwYdYY3tVIBcl0DCHP3/ADFxW1WyN2DJKzAW5uguENyZASCTm3Tlx3dYfDGo8sW5X0Un1nw2sxO/7aBnm9goxE1OYQ232GXlyiWtmWfR+fWCjCTaRVoekUQCkhVzjwkaEM4L8Y0wwxj+b3r9hcpcMus4BbJExKgNcKg49B4w5v03x4f8lL5u/KK7VSnEliD3c+qm/wDFoDUbXJfYqFpGls5YkSO1whROhdjuBYgt11jdgUdPpHl8v+0ZMt5s+zwLbaSFy0TWAJAy46eMDrksmCOauRmmbjOWP2A7FkSVkCYS5LAaZO9oz6HHgm/n5k/AzUzyxVw6FNpSwmYQkMBz3DfGbWQhDK4wXA3C3KCch+k2Hil4lLCSfdSWc8t8asfw9OCcpcvoTPVVKkrS7Ms06seBnU7RheGSyen5NG9OO/wGrdmzJTYwzwebS5MSTkgceaGR1FiwlkhwDaEqEpJtIY2k6KNAFnNEIREIdEIdEISIhAiZxBBfLKGLJJNW+uitqqhmVW91CCO6lWI8bu3mfGGxz0lF+/8A2Dt5sOmclQlJ3qBW+XvH/wBjDPVUlGP1/wCQdrVsLUSEqBVqcRca6Do+kHPHBrhAxk0ITaMjK/rrp0eMssLXQxSQAEg7jC1cWF2NS6lwx18OsOWW1TAcPIGbK1GXnC5QfaCUvBGLEGOcXe5U+yVT4CURX2iAiy8ScB3KcYfNoXKVRd+AkrP0JsyllmaqpMqWmfNCe1WgNiUGchyWchy2erx4f4l8Qy5pbbpLpHXx6eMFyuTeq6JE2UZc1IWhYZSTkRnfwHhGSOfLhqUJUwXGMuGjzf2/oqen2ZMkUjSpYnIWsMVdopwkDtFEk4XB/t5v6X4Z8SzZpqGVdmXNp1CO5Hjurx3vqZC6N5gl7sF+xxdRi+ZPgnCDhYRxPr97uEMUow+4NOXYvNmlRvCpTlLsNRovKplG7W3np9RBRxtkckhyRSpcA3KstAHD+oPlGiGKK75Fyk/AWsnpwljfurSBvJHgQAfGGZZxS4+4MI8itXW4iSA3unPIgHLhfyEIyZk+voHGD8i8+pUoknVn6ZekKyZXJv6hKKQJ4XYR9KuQZlE6LqRhKk64ciob2IvzEdvM3LRRS56/Y50Ft1DbBbdARIlS3dQSnFwVqniwA6mB1j26WONh6dXllNGdsIPOR19Ix/Dv/kR/Udq/8pg9pn9VfOB1nOolfuFgVY0b1XJUZ9MkDMd3joT5GOrn/wA/El7f8GHF/l5GxWiSDVrIuwUR0aFYqetk/ZMZO/wyQKesqplKUSf1CxPS3pC5y36We7/7BxW3MkvYrQ1JMiamzJSOd8UDpcjlp8kX4CywissX7kbIwIQqapIX3ggA8cz5+UK0ijHHLK1zwi87bko34skUSBOm437NAxEDPkIOWnxrNPd+VKyvVl6ca7fBRWz0mcQ+FATjJzZPzMBLSxeVrxSYSzP078vgGjZpMxSAoAJviNhf3RzLwH4O8soXSQXr1FSFvyamUrRNj6Qj0J02/AzfG6Bqp1AJLFlZceUB6U6XHZe6PRRSCM4Bp+QirRCHRRAiJpGp/wAXEHGckVSGJdb8QewHhb0fxhsM1PkFwDBaV5s532O/OD3Y5LkHlC8yn1BzyfdC5YvKCUgQUUwClKJdJnKY5RHT5IuCr+IgXyuQkfoJFPPpkS2ClJKEYkkYlJVhD53IfwjzvxH4WpPfCJvwai/lkMIqJ0/ustjoRgT11VyvGDD8MzSdVS9x0s2OHXZf2o9hZlTQzUp/3MOKWMhiSQoJbixF98ei0uhx6f8AL35Zhy55T7PCJ9bKVTCUuWUz5ZYKAbuvcK46dI3CDJF+UEuSixmtlBbq6K2+5MuSTwilBvstsaQhCc25nO/D7zh8FGIttsqqtAdg/E9fr6xUs1cItQFlzyWvl/n5wl5Gw0gTwuyzmiEJCYumyWXRJUcgT0gtkn0irQxSV6pdhlGjT6yeHhC8mGM3bBVVUpZc9IDUaieZ/MFjxqCpE0dRgUFAPn5xNPn9GanVkyQ9SO0pUTcSirJ4DNk9Sbn7lwjtVGrK24QhKSHKHwmzjEAFMdHAvHQhr4KKco3JdMzS0zt0+GJ7P2gqXOE0G7vGTFqduXfLz2OyYk4bQ209oJWkIQMKAoqYZAquW8vAQ/U6jE4eni67/UDFjkpbpdgaaoAlTEvdTeT/AFheHLGOHJF+aCyY28kZew1sqol4FS5nxIWD/wATcciHHhDNLPG4bJuuUwM0Hu3peKLyKpExc/GWExJY6Au4tu+sHjyxyZMiv8yKljcIw+jLieiZNnJBwhSMKD/xZn5tBKanknBPxVlODjGL+tl5C0LmTbsMUsjeUpIB6teDUlOc4r/8/sitrSj+v7mcZricd5DdVP8AKMe+45P0/ka1+RGkR/sgF8igcpaSOXePiI3c3BP9P9hVfmf99itSHVNSSLrQCeJdy/MGMsuXJP3QyPFfqTVUyStScIB7gDaOpsuUScMbb49v5oik0lz7gTRJK1gOAMLa5h7+cLeBOUkgvU4QObQAZHfmOIA9YCWnryFGdgTRqvkWfXc/08xAPDJF70DVIUNDC9kkFaKhZGsS5IlJl+2fMQXqX2Dt9iigNIHjwErPS/wS9jhWVJqZweTTFJA0XNzSk70pbERr3RkYFln6Br9lpmXyMCQmi2WhHE74hB9ohD8ufjPsIUu0phQGlz/1ktoVOJg/7wo/3CLIfBiLRAqVgZCD3KILVkKmkxHkbL2o5MtRyBMDtkyXQRFIo6NzP3ug1ikynJBBRbyPM7/p5wf4d+Qd4zK2clw5JDtuthf1h8dKmC8jOpqZOFJIBPa4Txdw3kIrHjhtTr/V/UkpO/0CSB+nLUwDTBfmVOPBIhqSpNLyU+2r8Dmx5qcCsSgDjPyvGnS5IKLUvdmfLCVqvY+Zjhm86IQl4hCIhDohDohCXi7Ic8UQkGIRHYoi4IRii7ISFRFJroj5JxxE2iEicbXyy4QXqT4d9dFUiO1N+MTeyUghqlOS9yQSdXGRgnmnd2VtRZNasEl7qIJ6FxE9adt+5NiLGuUWdi3zIV8hF+u/JSgkSmtLEMLwX4h+SbEW/OcPOLWdFemUmVAOkC8kS9oNS0nSKcoEpnIlO5FgA5f7zMLdeAlfk/Sn4I7EnU2zk9oMPbLM4Ai+FQSEvusl+sCWehLS4tFELEcYhBWokLPur6NEIea/i57HLrKYTUg9vTBSkpAftJZYrQ+eINiHUavFkPz7+XcEpLsHI1HHiIsgKWRrFxaXZTT8Be2GghnqRB2vyXFXw36wSzJE2HGt3AZfJonru7K9NFTWKvlf+cvHyinnkwtiO/PrtfJm6Bh6xPxEl0VsQNNQoBn/AHYv7t8L9SX72FtRUTizPZ3674nqSqibUQVxN7LopAEOiEOiEOiEOiEOiEOiEJiEOaIQ5ohDmiEOaIQnDF1XZdHYYqijsMFRC/Ym9jbO2/KL9OXsVaLijW7YS7kdQHI8IL0ZFblVky6JRAIZj8i0XHBJqyOSRIojvH2/0i/QkVvRYUX9Xl/MX6H1K3kKpwNfQcYr00uy9zYNSU73gXGKLTZ9Z+Hvs9+draemI7j9tP1/TSxCTucEJ/8AshQR+rAGyiiHPdohCYhDohCq0gxCH5S9upKaKuqaZMoMieqYhVwyFsoIA+HAoJ4s8WQ+XrpYTMUkZA25G48oshwlJOukN2RfkC2E/Jj4vL+YJYL8lPJRU0R+IefH6ecV6DL3ogUKuHjz/wDU+UV6En0XvRT8qq9jYBR5Fr+YgfSlZe5EKp1DMHNstd3OJ6Ul2ibkUwQO1l2iMMC+CzsMQogiLaa7ISlBOV4kYuTpIjddnKQRnaI012QPKoJik4kpJG/6b+kOhpsk47kuAJZIRdNgpckqOEBzuhUYOTpLkKTSVsNV0SpZAUzm8OzaeeGt3kDHkjO9o1J2OtUvtHSHyBIcjeBm3HiN8OhoZTx77Fy1EVJr2K7MoBMClKUEJFnOpOQ9PGB0+mWTc5dIvLmcEkl2RT0STNMtasLFranQecFi0sVmcJvouWV+nuiWo6ZHaLxglCASQMzoIvHgh6s0+kVLI9kWu2MU9IhK5mIYkjABdvfIY8WBhsdPCOSSkrSr9xcskmo19f2OlUqcC0kAqKpgB1GAPbzi4YYKEo123X0roqWSW5fp+508BKZSgkd3AMs8SQq++7wOTbGMJV1X8BK3KS+/8lkgBM4FmStTjkRh9FeMFwozVeXZbu0RXTgJirvZCi2RKVW/8TFZJpSa96/ZlxjwgS6pAWS7hwx/tIJ8WhbypS7LUHtAIr2SwT8Xnl84Ss6SoP07YJVWS+Qu/i/1gHmb6RexHfqKfPjp95xVzkXUUcaY6nnFvE/JSkvAOYgOwufu0BNJFxbPbv8A4/7O/wCor5qkkKR2UpJI0UVqUAeSJfiIWEe1xRCn7ukQheIQ6IQ6IQ/MP43ofbM4DMpkgcyhIiyHw+0pgVNWRk7DkLD0iyFUyXDgwxY7XDB3USErTe/MZRGpRJwzk1SgG0+/rFrLJEcUGlV7ZjefEEep8obDUV2DLHYX80glZuHAYeR9T4CLWWLv7FbHwHROSQnvX7Uq4sMV/SGqadc+bKcf4L04/Tl5G6lD/kBMJt/2eUOhtaX15/kXK7df30L1FPimTLfvI66+cZpRjOTf1HRfyoe2VLlypPbTElT5AEA7gASC1+EbNPjhh0zzyVt9GPNOWTL6UXQttunSUpmpDBTecV8QxRljjnh5D002pPHJ8onYFWlJCMAKlOCTua3nFfDs0ItQrlk1WKUouVmftX/dXz+UY9dGs8h+nd4kfQTKlUsyJST3FNiG/Qesdec5YpYorprkwQiprJJrlMxK8mXOVhsQT55xy9W3h1LcODbhqeJWG20okSVEuSgX8Id8Qe6OOfugNMqlNL3NKnlkqpSPdKFB9O6kFT+UaYyW7C11VCZK1kX1EqOUVypyENiCgoB2JAN23724QjGt0MkId3/yNnxOMpdUC2msfmiUlwFpvvZrwnUtfil+lh4o/wCDX3OlzkCdMCz3FhSSRmHyPQtF74rNOLdKS7Jtfpx90W/1FAmrJDoISm29DYVDqnzMR6mHqyT/ACtL9i1ie1e/P7gBtRQEwW76irkSCC3MEiFR1dbuO+gvS6FptWpSUoJsnKESzOUFD2GLGrsoqaovfPPjFPJJ3b77LryUY+EBTaJaQyijU7K7t0gvxyLaiG/h5dS4B3rwHkUIL4ncEjhkCk8jDceCPkGWT2LrCEHQZ8d9j1t1G54uW2BSuQCZV7hfefp59YCWb2CUPcH31nh4CFrfPoL5Yn3HsR7AoqpZmz1TEg+4EYUn/kSoGz5cnuDHA+J/Fvws/TxK35s26fS+orfB6F7C7Rl7JnrpKlRCKlQVKqFEBBUkBHZzPgUwTfI8HYatBro6vHuXflC8+F4pUetAxuEFf3dIhC8Qh0QgjtTaaZITiclRYANzOf3eMms1cNNHdP8AYZixPI6R+bfxcqFf6rNmkJdSZZR/SkJCBiA/c6T0aGaXUR1GJTiVPG4S2s+TokSpoUlSCFt3MBJJUck4S7kndGhtJWwBespZsiYZcxKkLSbpP3ccdYrHlU0pQdpklGnTJlVQyPl9I0xzeGLcPKDmWhd7G2ngH64fGG7YSKtoH/p7+6eh5t6XgHgvov1BVUlQuxZyPDOEvHKr8BWijQHQRZE5SSCCQ2UHGco1XgramFlVakixzL9YbDUyivALimbgkmZROkPgAKmzAdnbc4z4iOnNqWhS+n8GFLbqmwe0UgUclzch23B7eLPybfA5pf8AgxTDxx/8iTMrZS2moP8AVHP0TrPH7mnOrxsttofrKbVjDfiK/wAdgaX/ACkjap6qUtElSrLkkHgoDRQPEC+626N0fTzRhNy5iIcZY5SSXZhbRqO0mKUbuXjl6vIsmRtGvFHbBItV1QUiWnVIaDz6hTxRh7AwxuMpP3L021VoQZYPd/zdup8YvDrZ44bEiSwxbsUlT1JLgsYzwyzg7QxwTXJRSyS5zgHJt2+wqS4RUmKbsh0UQNJplKcpSSwctoIbHFKStIGU4rsMKE4EzHscwMwAWJbdDfw72KT6B9RbnEakUkt1puQQFIVrhe5YZkbuBh0cONNx8dp/QW5ypP8A3+4aoSwxEAAMiYA2liLbiHB1cboPIqV14plJt/yLT6pLDVQcHcU5ON2/nCZZor6+41RFZtYpRfJxhLajjCJZpNhKKKIlqVoTx/kxSjOZbaQ7Io0ghy7sNwuc/v6Qbxxim/KBUraR7bs/2RpAhP6KCQ1ykE8yTHgdR8X1TnKO+lfSO7DTY1FWjep5CUBkhhHKyZJTdtj0uKRm+1Ow0VkhUpWeaTqFDIxr+H6uWnzKS68/YVnxLJCj438P/wATp2z1/k67EuShWAKN5km7c1yxuzAyswj30JxnFSXTOI1To/QcpYUApJBBAIIuCDcEHURZRaIQ4xGR9HxvtTPKlywdFlvAxxfjn+VF/U26P87PM/b/ANjlVU0TULwrwhJBDggORlcG5jF8M+JRwY9k+h+o0zyPdEL7D+waKdYnTT2kwXTZkpO8DU8YrX/Fnlh6ePhP9yYdIocyMX8V9kqFQmfheWpAQToFgn3tzggDk0dT4BqMc8HpPtfwZddCSlvR57OpCLi+/fxjtzwuJiU02LpURlCk2gqGpFcoZsf/AMkD6xohqJLsFwsOiaCgJe4Sc7XUcPWylH/EMg04JLv/ALAaphK2QCrCAx7kscySXPFmEHlgm3x7IkZFKjZg76kqdKUg83Dt4eogJ6ZfNXgkcnSM+ZJZn1APQ5Qj0WNse2XtZUl8LtfItnYjkd0adNrPRW2StCcuBTd9MDX1xmcAIHVav1lS6ReLCociqFEMRmMoyRk4u12OaXTJmzCouS5i8k5Te6T5KjFRVIHAFkxCERCHRCF0pJygoxcnS5JddhJNOVKCRmd9m5wcMUpSUfIMpJLcNS6HDPEqZk4BbXlGiOn2Z1jn1/IuWW8bnEdkS0S5oWn3CVI718KtH3jKNUcUIZNy66r2YpzlKNee/wBCwThN/wBPH3VaBMxBBBYftNj1i01Ft9Xx9mv6lVuXvXP6Mhc9CFlK/dIxBmIBUGWgtml3Y8BAymoSqfC/r2vsXtlKNrv+6ZlJqlAJAJdJdJ1D5xg9WlXs+DTsVgpk4qJJOecBLJKTtlqKSJlSSosBe58LnOKjCUuiOSQ5IoX171iNzi6kl9RGiOBdXyA5h11aQnK9+7uvccs8v4DHljt/4A2O7M4zVKIAfOw4n55Rjnkb76HRj7H6R2SD2ScWbB4+aahr1XXXJ6KN0vsOQksiIQ+K9q/YBFbUy1pnJp1L7ilFGIKP7ciGUzjjaPUfBNfx6E/0/oc7WYf9aPY9h7OTTU8mnSSpMqWiWCWchICXLa2j0pzh6IQQ23tmRSSlTqiYJctOZPkEgXUTuEQj6PHNk+2K9pV0xYGCQhhKQfeu7rX/AFEAWyGQ1J4vxt/4UV9Tdol8zZ9wZYOceUTpHRJCQIptsgrtGVKWhSJoSpJDEHIiG4J5MclKHDKlFSW19HhXtVSSpFSZUsky2BvcpcnuPmQ2+9xnHv8A4dq55cK9VHD1GKMZ/IZc6QFuRaxvoc/U26R0JY4ytoQpNGfMlEZ9PT1jLKEojE7KgwJYxIq1JI1AVibeefUw2OWUWBKCaGVVoKFDJSiQB+0JOHU7gkCND1ClF+7AUKkC2iP1CxBAYBtwAA9ITqpVkaTGYvy9CUZwiIhDohDohDohCREIHm0i0pCilgcofPTzhFSa4fQEckZOkPbOo5RlrmTCWSQLdPr5Rq02nxSxSyZPDE5sk1kUI+RjZ8nsahLkEKHcVYi7NDsOKODUV4fTAyZPVxOu12UrZalIUshpkshK9HByVbkYrOnKLl1OLp15ReJ1Kl+Vi5X2koF+/L806HoYTu9XDu/1RDS2TfswtRtJCpShhZasOLcSlwFcCxvvtFy1MJY23+Z1+3kqOGUZKukJVFctaQlSnbJ8+F4zz1MpwUWOjjjF2hbEd8Z22+wy8qWVEJTcmwgowcnS7KbpWx6jowQFG5CmKMrWs+838I1YtOmrl2vHv/2Knkph5yMASRZBJKSLsrfxSdQeO67ZVDrr+P8AoGL3cPsTqqxz3Rhte73GRBzjNkzX0MjETKiYzttu2MNT2cwpqJcyYHQgurVs8JbMgKaF5sWSeKSh3QUJxjNWe4bL9opS0jCtKuRBjwmfQZsb+ZHbhmjLpmrLr0HWMksUl2NtDCVg5GFVROzO28odkQY06W1kTQMknFpnnlP+L20aWYqWVy6hCVHD2qXUA1hjQQS28ubZx9BwtuCbODNVJjFX+OtepLIk08s/FhWryUpobQNnn+3/AGiqq1YXUz1zVDJ2CQ/woSyU9BEoh9j+FawjETqr0YRwPjScqR0NF5PVzWoAzjzO06B89t/2pRJSSVAAfbDeY26bRSyypLgXkyRx8nntf7cTJxKZbpG8tiI1bQefRjHp9H8HwR5ycs5mbWTfCPjatCgcSiS93JJJ5nfHUnj2KkqRlUrKyagp5bvFj0d4kMjiU42aspSFhtLW1CUtnuDnwPCNy2TQl2mZy6UkY05FTJGrXb0bpGV4W05L9Bql4FTCH9QyHiiHYohLIiEOiELJS8Wk26RC82QpPvAh98HPHKDqSoqMoy6NTZFDKUhcya7JewzsH3jfvjdpNPjnjlknzRmz5ZKUYxdWC2hQhITNll0HqxianTRhFZsXMX+xeHM5NwnwxqlqzUBUpZDs6OB3Q/T5/wASnil34FZMawtZI/qK7LqBLUqXM9xXdVw4xm0uT0pSxZOnwx2aG+KlDtcjm00JRJSgLCylRKVBw6SzAg5Ed7xjRnhKGnSbXD4+wvG92VtLtcis7bKlowqAJbCVMASBk7C7cYz/AI35Gq5fFjfQp3fBl4owXXQ8gRCF5UsqLAOTpFxi5NRiuSNqPY7S0IOPGSkpALM+rEkbhGrHpr3KfDQqWWqoflU2ICWwC0jNOd7pmAj3kl2O7ONnppx21z7rvnp/YRuae7w/7oRFaUnFksWU9woDIniN8Y5ZNr+b8y4f1HqCf2E508qJOhLto/KM+TI5N/wMUaBQssZpqYq4C4BLs/wvvvDYY93LdAylRoGoSgMQxGmnNJvudo1+osaqhW23ZmKnqxYgSDvFj5Rgm1O7Hrjo2dmbcqU37ZRAyCu8/jfwha+H4cv5ooL8ROPTN+i9v5ks4VhxvSX8jHL1PwPG3/hs1Y9bLyG2p7aGahkvd73EBpPgjhLcwsmu4pHn85ZUok5kkx26SdIxXfY3UpAQ2to0ZUtgmL+YUpxeER7GPo1dkbVMhRGjvbT+Iz6zSrKOw5dh9JP9smTqTujmf/yWnZq/GKj5yr2gqocqz0D2HH6/4EdzS4IY8e2KOflyScrZkKBSdxicxZO0aUuYJg72jOBnfdxJ8GjUpLJwxdbWITpJTdraHQtm0ZpwoYpA0LIyLPbpugE2lwRqx+XUgpawKU2v7yj3X4WJjbHLGSr2XAtxd37hqqmSAlDNhClKOrAAX5qBbmIPJjTqL+7BjO1ZnLplBIUQwOUY3ikoqT6GqSugTQoILS0xmKCU5mHYcLyzUYgTmoK2alZ7PLQM3IDszZ3jfP4XJRuLtmaOsi3TEtn1AlrdSXIy4GMmmyxwzbmr/qPzQc40maVf/wBRK7UABScwNN8dPOlq9P6ke0ZMf+Dk2PpiuwqsJUUL91YY84yfDs8YSeOa4kO1WJySku0asrZ5lJnS1sqWoAy1BQIfEkHiDhxWIGUbcGGUN+Nr5ROSak4yXZ8zLmlJBBYg2McWMnjnuj4ZvlFSVPyFrqjGrEzPnz3wepzLNLdQGOGxUL4oRfgZSIiEJiUQOumKcOMEAsekOeGWNreuwFNNOjYXTJRMCpIIUkBYBPvpZ1FJ3i8dGWKMZXDtK/o19DIsjlGp+ePsyZl0dqhYJTdLkYgNZaxrwNxYxJNSi5x8K0339Uwkv9LXff8AVGbW1+PCUpwFIaxPNhqA5MYsuoUknHhofDHT5EVLe8ZW23bG1wREINU9I4xKcIvcAG44PlcQ7Fi/1S4XuBKaXC7Hpik4XsktZh3F6NYNpqxBjS2lG/7YCTszJ84qzJLZXJYbg+kY5zcnyNSorKQScieQeBjGy7o1jMSmXYgtZvmUnz4xu3RjARtbkZBvGGT3MeaM5OFDNo2ue/1jXL5YClyzPQHI5xkiuUMfQ9XHuswF949BGnP+VC4LmxGWWI6Rmj2MGa1LEHfDcyaaYMGFQMUr7zH8QaqUCumKSJuE+v3l/iEwltYUlYzWSnDi5uS1w2/lxh2WFqwYsUlTCkuPvSEQk4ysNqzXQUzEtYDXUpSPTLw5X3rbNCOYsyZkvUA4XLHfGGUH34Hp+AYMAuOSxqXUuFBVypu8SXYeungI0Rz8NS5vyA4rv2NaaQVYbLCLgA2csiWnoznrG/htJc14/gzptR5MuvSO0XgHdxEBo52dN5HtQ+H5VYbY6uzngK/4nr9iNWifo6hKffQrULfidD1atUiox5pXnuOh+sas7lptSp+H2ZsKWbBt8oB7SUXZrChkoJV0UAoHwMJ+I4o2ssOmP0mRtbX4FtjVvZqIPuqsfkYToNR6WSpdPsPU4t8bXYtWpSFnCQRnb0hWpjCOR7Xx4GYm3FWR+bW2HEWgfxWXbtbL9KF3QAxnDOi7IcBEq+iBOzIZwR0gtjTSkUmn0bNVsyU4QhRxlOIPkrOwLx1Z6LFahHh9r6mOGfJ+Z8r+AEuqxnspx4An9ivoTn4wiGbe3iz/AG+wyUNv+Jj/APZ0ivVJ7ikhWH3TcFPFJF24ZRUc7wvZNWl0XLGp/NHi+zMmTHJOTkxinPdJtD0uKKQBZwEQg3SSH7wKSQR3DmrW3hGnDi3K/Pt5Yuc6dfuaaZqQCtLBi5Q+E8Q2h4ixyIjZuSTcePoxKi75MepnYiSAwJdo5+Se6Vo0xVARCizUoqchOJLF9QSCP6SCGvuMbsOOo7l+3gTOXNMWr5+JVxcasx63hGadug4xojZ8vErJ2vr0yBisEN0iTdILtJIDAZ63dudnBh2o6oqAtSJ76efL5GEY43JWFLod2lLZIsQX1xf4jRqIJR4F4nyZojH5HD1WcSAeV/8AFt2sacluFi48MpQKDsfVunHPKB07Vuy5oFVpZRA9G8tOUBljUi4vge2bNB7pud17jcWyAv49I04HuVMCa5sRqkAKIBcb2aM2VK+A4vgpLmkAhyAc+I+cVGbXBbRqVCwpICQSgHCgMzqNvADzPGNc6lFKPXQpcPkz6ulMssSCWe3GMuXFsdDIyT5F4UEMUlYqW+Fg4bLzG4w7Fnljtx8gTgpVfg1tmVEpEsAqDm5cHOOtpMmCOJbnyZsiyOXCMufPxgE+8LHiNDzjmZc3qxTf5l39TRCG3hdGzSbZlrl9lPQF7jcKB3hQy5EERvhqsefHszeDK8Esc9+MQ2xXJWAlOQAHRIYDwgNdqISgscPAzT4nFuT8mXHKNR0QhEQh0QgxR0qpisKReHYMMs0tsReTIsatl5aezmjEPdIfk8HGPo5ql4I3vhwb9csLWErCTLmNgUABhNgH6+sdfO1e3IrhLp+UzDjTq4upLte4l26UEyZ4UcB7qkllJ5FjaMrmof4OXx0/I7Zf+JDz2hHa9SmZMKhrmd53xl1mSGSdx5+o/DFxjTElKjK232NorAkOiENGjpMSMeMApULEdQSdBG3Dg3Q3t9CZ5alsrvyP1ISsntCEKZ72IOmEgMtPDjGuajPiXf8AfQqCceY9fyY0+cVZlyLPr1Oscyc2+zTFJdAYWEN0FO5dWIJ+IBw+j8I0YMak7f7C8jaXA7WBSRjcF8lDuq8UliI0Zd0bn3/IEKfBkFUc9vmx5o0Mju4u+H+HIjpfPhGvBj+W3wKnLmhWtU6veKmsHDeUJzO5dhx6JoUurNQsbpBJ8omGNyKm6QeuSyRdZ4Ky6WHpDc8aXZWNu+jPjKMNFBKpeEB7cSbeQjUm3joU6UrEpS2UDu3FvOM0HUhj6HatBUkEAMnczaa/uOUacsXKNgRdOhBCyMiRpbdujMnTGPo0p7KSEpBY+4Guo6nkL/eWyVSSSXYlOm2zOmJILGxEY5RcW4sbdh6OpCS6nIvZ2uQzw3Dm9OXPK5AnG1wNzJalMLBUzvPolAyHABn6CNUot0n3Ll/ZC1JL9P5Eq2nwKKXewPiAfnGTNiUJUmOhLcrYtCQizxdks//Z"},
                        "buttons":[
                        {
                            "label": "first button",
                            "action": "message",
                            "messageText" : "first button clicked"
                        }
                        ]
                    }
                }
            ]
        }
    }
    return jsonify(data)



if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
