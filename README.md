# StakeChain

基于PoS共识机制构建的区块链系统，提供节点之间P2P通讯，支持RESTful API接口调用。

## 1 使用方式

### 1.1 环境安装

```python
conda create -n pos python=3.8
conda activate pos

pip install -r requirements.txt
```

### 1.2 执行方式

```python
python main.py localhost 10001 5000 keys/genesisPrivateKey.pem  # genesis抵押
python main.py localhost 10002 5001 keys/stakerPrivateKey.pem  # alice抵押
python main.py localhost 10003 5002  # 无抵押

python interaction.py  # 或者使用Postman
```

![](/assets/image.png)

### 1.3 执行效果

#### 查看节点中区块链数据

节点10001: http://localhost:5000/blockchain

节点10002: http://localhost:5001/blockchain

节点10003: http://localhost:5002/blockchain


```json
{
    "blocks":[
        {
            "blockCount":0,
            "forger":"genesis",
            "lastHash":"genesisHash",
            "signature":"",
            "timestamp":0,
            "transactions":[

            ]
        },
        {
            "blockCount":1,
            "forger":"-----BEGIN PUBLIC KEY-----\nMIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQCpQ2c9UvIiDOdU4i4yZG0Swyf2\n8ylVMePPSTL0Lqh3Z8gcorYbMLEalUjXPIvuIcdRzjzVUDFt9wWPE4m0InaZH/ul\nUSpEiWpX6zbkrcXsSnVg6v4gHROrYoE0ZkvmuVUAKr/KhXe3S6SN75WQABJG9Ew9\nJhG1hlWvS9TiCqIr6QIDAQAB\n-----END PUBLIC KEY-----",
            "lastHash":"9994ee14250c7b1b010d717f85dac23fb493f58857c51e85bd855530885bf9a5",
            "signature":"8dbbfc9b5cf4f9cfc1f2ff5d77f86bf3fa38222a07fb0428341220803a215cf394b63fabf8bbde9fb12ef42e2463919b952e0397ab0930fbd0cfb8b40b3db517f76e9b769b9491fe2c9fcb58acef268fcf7207c069471827a85928aa2938a286449044fe9e6d11feaded24ff16ff5d6ab838078fb5860c490b1d1bf4c8062a7d",
            "timestamp":1696224862.9887369,
            "transactions":[
                {
                    "amount":100,
                    "id":"54047cb260e511ee8d41b40ede173ee2",
                    "receiverPublicKey":"-----BEGIN PUBLIC KEY-----\nMIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQCz5GsVfnrZJdX+121CA8e2pa0s\nSDPIgAkWoruT29I14NYPnK77BwIxTxUFfa68BT5uLCqmrG3Et8mfSuNNhdhrJJOZ\nZVdKll5JEomvpLCmImbNPyWxjTA75w7R7cUeLL6oJh7UChKKrZs+T2/7WqpmGw7u\nO0OFWWc8/Eh3MD7ISwIDAQAB\n-----END PUBLIC KEY-----",
                    "senderPublicKey":"-----BEGIN PUBLIC KEY-----\nMIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEA3reyZyELSrXT8labYOJy\nX3LheYbXP1CzlHYLT8ZUibf5oyiwDZ47J6YvaHLt5aHOz+ki13w+2SnXD6+pIbJi\nFJBZVWuZfT87efdpBdAdP9Is1BUjbow437+VMhWG/uBJB2CgOemYPxVJ2x0u0zS3\nU1/wJxrW0JizxWKNn6e7ISGFsZVKvRuVK/6KIO4kR43dwsIN3l2jwHgyU1b7t2Qi\nlILVua+5ICayAFWxQ0jlt2NrryXI7zuDV6xKBj9Ula3DEgau6MAvj1NIuCZTv58b\nQPUCxpacGpggwJcvMdW0sugNgCPV/KiZN4OYVjNXAG5eqodx/CAZtlVrMOVdcoLZ\nfwIDAQAB\n-----END PUBLIC KEY-----",
                    "signature":"1eb508bd194174b006492ef4c5e22af6189473b7a18b7f3982f7ac4c7194de4281ba50d38edb66d877c3714b92da1e995067f4dec6833465e601c551a1323b419d2e76e139bf4995fb1c4a77bab280838be4987584a33f978a3d36d40c55f04ac4ba061ee64a332fda916344a13459916fb0537f3670c829c75f053ead51345155f0be2fa83cca470d2b1b70af4290a0047a85667c40d219b424477d34dc88b816269b091afd70a1db9959ad78792ab3586c91f2309bf3266ec41970d71262f50fc6170d71a62c99a55e607e408f4dcba91e568e233ab5b262a474813f72cea0490bccb00a167671840bc556b03b6ab4d6b228ca2e764552624d3f95af1d70c3",
                    "timestamp":1696224856.8421555,
                    "type":"EXCHANGE"
                },
                {
                    "amount":100,
                    "id":"553e025860e511ee8831b40ede173ee2",
                    "receiverPublicKey":"-----BEGIN PUBLIC KEY-----\nMIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAxmtFyZJhpSZLuc8zPTkj\nUAkwVOTsXTzsOrZxKRDcfMlInsBWSz893VDuYsstfj9SlEoJyBtZri9cOUaZGSis\nzWCPa2x1QVs5S96ULQmtLGdFR6psFC+UxIIxrAkqIcPQa6632Kja8GfkuSA933sd\n9J69FRhcPLSlIDunnyL2UPv3rMqklTVyrVonPioF2dUoJb9Yruf80qsPdXt783Dr\njOR69xXXiqN/xQM2tih3eiNDDVy82CHpprhP3i5xaztUvDqZO3W/YvcatfOLgRsn\nyVuvVNEI4aYmbx2n+fzaXqWrOYdHiyoRKeAi1+6JdxU/oT9mQmP6nIKymx6xEWbU\nPQIDAQAB\n-----END PUBLIC KEY-----",
                    "senderPublicKey":"-----BEGIN PUBLIC KEY-----\nMIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEA3reyZyELSrXT8labYOJy\nX3LheYbXP1CzlHYLT8ZUibf5oyiwDZ47J6YvaHLt5aHOz+ki13w+2SnXD6+pIbJi\nFJBZVWuZfT87efdpBdAdP9Is1BUjbow437+VMhWG/uBJB2CgOemYPxVJ2x0u0zS3\nU1/wJxrW0JizxWKNn6e7ISGFsZVKvRuVK/6KIO4kR43dwsIN3l2jwHgyU1b7t2Qi\nlILVua+5ICayAFWxQ0jlt2NrryXI7zuDV6xKBj9Ula3DEgau6MAvj1NIuCZTv58b\nQPUCxpacGpggwJcvMdW0sugNgCPV/KiZN4OYVjNXAG5eqodx/CAZtlVrMOVdcoLZ\nfwIDAQAB\n-----END PUBLIC KEY-----",
                    "signature":"b227fbfd0f15b76b18e514b2527eb5d53f54f55e38fe8d76723c6d71c0400c116ced7991075e7a12020c9243cfe3b96b57863c451d02f458573db86372005352b3c81634e830b4be0d2de072ee49828f78ea9716e0e648ecc987489a5f9fa469f9e290a912b49a9548c05dd9fd0210f009395a5c87b390a68094a60e4610ba8db50f0ce7b0607826229f43cf4e97204e9c39caa93eaef5b9643f9546f192f8eabf256540ede00c0b716aedda4113952bf133da20c65604b6a79ed44da8ca53a82a86e2a1b59f2b8624895d0b3eeb8756de44c78aacab0fa27da0114b3b32790e3473699025d2515e79118188d6d7788374a317ca376ec0b552259fcb11fc8cd8",
                    "timestamp":1696224858.8968534,
                    "type":"EXCHANGE"
                }
            ]
        }
    ]
}
```

#### 查看节点内区块池数据

节点10001: http://localhost:5000/transactionPool

节点10002: http://localhost:5001/transactionPool

节点10003: http://localhost:5002/transactionPool


```json
{
    "0": {
        "amount": 25,
        "id": "5677bf0860e511eebc99b40ede173ee2",
        "receiverPublicKey": "-----BEGIN PUBLIC KEY-----\nMIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQCz5GsVfnrZJdX+121CA8e2pa0s\nSDPIgAkWoruT29I14NYPnK77BwIxTxUFfa68BT5uLCqmrG3Et8mfSuNNhdhrJJOZ\nZVdKll5JEomvpLCmImbNPyWxjTA75w7R7cUeLL6oJh7UChKKrZs+T2/7WqpmGw7u\nO0OFWWc8/Eh3MD7ISwIDAQAB\n-----END PUBLIC KEY-----",
        "senderPublicKey": "-----BEGIN PUBLIC KEY-----\nMIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQCz5GsVfnrZJdX+121CA8e2pa0s\nSDPIgAkWoruT29I14NYPnK77BwIxTxUFfa68BT5uLCqmrG3Et8mfSuNNhdhrJJOZ\nZVdKll5JEomvpLCmImbNPyWxjTA75w7R7cUeLL6oJh7UChKKrZs+T2/7WqpmGw7u\nO0OFWWc8/Eh3MD7ISwIDAQAB\n-----END PUBLIC KEY-----",
        "signature": "582d25389329f3ab3ee4b5bd66e23b977e1b748c1b503b836af05fe6722a8256d276a8fff4d842164f77fdc1834b52d5d49af87c08e87e62120866978615cdd835b42151e99ab3537f1f658379a1e3588d27f4f4632a39d837f9b26b36b31b9ff6b7ba89a0476d64da1c1dddfebc841d347afbeb6a463494ad33e89a1dadddb6",
        "timestamp": 1696224860.9529607,
        "type": "STAKE"
    },
    "1": {
        "amount": 1,
        "id": "57aefdca60e511ee8898b40ede173ee2",
        "receiverPublicKey": "-----BEGIN PUBLIC KEY-----\nMIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAxmtFyZJhpSZLuc8zPTkj\nUAkwVOTsXTzsOrZxKRDcfMlInsBWSz893VDuYsstfj9SlEoJyBtZri9cOUaZGSis\nzWCPa2x1QVs5S96ULQmtLGdFR6psFC+UxIIxrAkqIcPQa6632Kja8GfkuSA933sd\n9J69FRhcPLSlIDunnyL2UPv3rMqklTVyrVonPioF2dUoJb9Yruf80qsPdXt783Dr\njOR69xXXiqN/xQM2tih3eiNDDVy82CHpprhP3i5xaztUvDqZO3W/YvcatfOLgRsn\nyVuvVNEI4aYmbx2n+fzaXqWrOYdHiyoRKeAi1+6JdxU/oT9mQmP6nIKymx6xEWbU\nPQIDAQAB\n-----END PUBLIC KEY-----",
        "senderPublicKey": "-----BEGIN PUBLIC KEY-----\nMIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQCz5GsVfnrZJdX+121CA8e2pa0s\nSDPIgAkWoruT29I14NYPnK77BwIxTxUFfa68BT5uLCqmrG3Et8mfSuNNhdhrJJOZ\nZVdKll5JEomvpLCmImbNPyWxjTA75w7R7cUeLL6oJh7UChKKrZs+T2/7WqpmGw7u\nO0OFWWc8/Eh3MD7ISwIDAQAB\n-----END PUBLIC KEY-----",
        "signature": "85678e4e4096a5083d315a2376fc02f46af486f8f26b5629f65ee3eb4030d89cf58ed5342e07762810ab2d5fe963d0d47286ec30341bd68061d74c89d268dd9ed835fe13b0d1a5bdffef5b3c40a14a52ce88f55a7a543435fcdc676006dd2d5cc5912fdd45699332483eafab2979988dace327ba44b036f69769996a1b89cb8a",
        "timestamp": 1696224862.992737,
        "type": "TRANFER"
    }
}
```

#### 发起交易


```python
python interaction.py  # 或postman调用RESTful接口
```