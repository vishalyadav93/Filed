import requests
import json
import unittest
import scratch

class TestCases(unittest.TestCase):

    def test_validate(self):
        type='Song'
        payload= {"audioFileMetadata": {
        "name": "test",
        "duration": "120",
        "uploadTime": "12-03-2021",
        "author": "xyz",
        "narrator": "testp"
    }}
        response =scratch.validate(type,payload)
        assert response !=None

    def test_get(self):
            response = requests.get('http://127.0.0.1:5000/get/PodCast')
            assert response.status_code == 200

    def test_create(self):
        payload=json.dumps({
                    "audioFileType": "AudioBook",
                    "audioFileMetadata": {
                        "title": "test",
                        "duration": "120",
                        "uploadTime": "12-03-2021",
                        "author": "xyz",
                        "narrator": "testp"
                                    }
                })

        response = requests.post('http://127.0.0.1:5000/create',data=payload,headers={"Content-type":"application/json"})
        assert response.status_code == 200

    def test_update(self):
        audiotype='PodCast'
        id=1
        payload=json.dumps({"audioFileMetadata":{"name":"test","duration":"123","uploadTime":"abc"}})
        response = requests.put('http://127.0.0.1:5000/update/'+audiotype+'/'+str(id),data=payload,headers={"Content-type":"application/json"})
        assert response.status_code == 200

    def test_delete(self):
        audiotype='PodCast'
        id=6
        self.test_create()
        response = requests.delete('http://127.0.0.1:5000/delete/'+audiotype+'/'+str(id))
        assert response.status_code == 200