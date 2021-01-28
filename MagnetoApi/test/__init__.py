
import requests

def test_decrement():
    assert 5 == 5

def test_get_check_api():
     response = requests.get("http://127.0.0.1:5000/mutant")
     assert response.status_code == 200

def test_is_mutant():
     response = requests.post("http://127.0.0.1:5000/mutant",  json= {"dna":["ATGCGA","CAGTGC","TTATGT","AGAAGG","CCCCTA","TCACTG"]})
     assert response.status_code == 200

def test_is_not_mutant():
     response = requests.post("http://127.0.0.1:5000/mutant",  json= {"dna":["ATTTCA","CCGTGC","TCATGG","AGAAGG","ACCGTA","TCTCTG"]})
     assert response.status_code == 200

def test_get_report():
     response = requests.get("http://127.0.0.1:5000/mutant")
     assert response.status_code == 200
    