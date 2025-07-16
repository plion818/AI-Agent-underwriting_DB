"""
{
  "customer_info": {
    "customer_id": "C00009",
    "name": "李彥廷",
    "gender": "男",
    "birthdate": "1982-06-15",
    "age": 43,
    "occupation": "設計師",
    "marital_status": "已婚",
    "contact": {
      "phone": "0911222333",
      "address": "台北市大安區和平東路50號"
    },
    "health_status": "良好",
    "smoking": false,
    "property_proof": "月收入5萬",
    "希望購買保單": "財產保險",
    "credit_rating": "AAA",
    "credit_alert": {
      "credit_card_overdue_count": 0,
      "bad_debt": false,
      "joint_credit_warning": false,
      "over_insurance": false,
      "duplicate_insurance": false,
      "abnormal_insurance": false
    },
    "claim_records": [
      {
        "total_claim_amount": 50000,
        "disputed": false
      }
    ],
    "criminal_record": {
      "has_record": false,
      "blacklist": false
    },
    "suspicious_transaction": {
      "money_laundering": false,
      "terrorist_financing": false
    }
  },
  "rules": {
    "財產保險規則": [
      {
        "rule": "基本資料",
        "keywords": ["property_proof"],
        "required": true,
        "class": "財產保險",
        "description": "月收入等財力說明"
      },
      {
        "rule": "信用評等相關",
        "keywords": [
          "credit_rating",
          "credit_alert.credit_card_overdue_count",
          "credit_alert.bad_debt",
          "credit_alert.joint_credit_warning",
          "credit_alert.over_insurance",
          "credit_alert.duplicate_insurance",
          "credit_alert.abnormal_insurance"
        ],
        "required": true,
        "class": "信用評價",
        "description": "客戶信用評等及過往異常警示"
      },
      {
        "rule": "理賠紀錄",
        "keywords": [
          "claim_records.total_claim_amount",
          "claim_records.disputed"
        ],
        "required": false,
        "class": "理賠風險",
        "description": "歷史理賠次數、金額、是否曾有理賠爭議"
      },
      {
        "rule": "犯罪紀錄",
        "keywords": [
          "criminal_record.has_record",
          "criminal_record.blacklist"
        ],
        "required": true,
        "class": "風險控管",
        "description": "有無犯罪前科與是否列入黑名單"
      },
      {
        "rule": "可疑交易",
        "keywords": [
          "suspicious_transaction.money_laundering",
          "suspicious_transaction.terrorist_financing"
        ],
        "required": true,
        "class": "法遵管理",
        "description": "有無疑似洗錢或恐怖融資紀錄"
      }
    ],
    "醫療險規則": [
      {
        "rule": "基本資料",
        "keywords": ["age", "health_status", "smoking"],
        "required": true,
        "class": "基本資料",
        "description": "年齡、健康狀況與吸菸習慣等基本資訊"
      },
      {
        "rule": "信用評等相關",
        "keywords": [
          "credit_rating",
          "credit_alert.credit_card_overdue_count",
          "credit_alert.bad_debt",
          "credit_alert.joint_credit_warning",
          "credit_alert.over_insurance",
          "credit_alert.duplicate_insurance",
          "credit_alert.abnormal_insurance"
        ],
        "required": true,
        "class": "信用評價",
        "description": "客戶信用評等及過往異常警示"
      },
      {
        "rule": "理賠紀錄",
        "keywords": ["claim_records.claim_count", "claim_records.disputed"],
        "required": false,
        "class": "理賠風險",
        "description": "歷史理賠次數、是否曾有理賠爭議"
      },
      {
        "rule": "犯罪紀錄",
        "keywords": ["criminal_record.has_record", "criminal_record.blacklist"],
        "required": true,
        "class": "風險控管",
        "description": "有無犯罪前科與是否列入黑名單"
      },
      {
        "rule": "可疑交易",
        "keywords": [
          "suspicious_transaction.money_laundering",
          "suspicious_transaction.terrorist_financing"
        ],
        "required": true,
        "class": "法遵管理",
        "description": "有無疑似洗錢或恐怖融資紀錄"
      }
    ],
    "壽險規則": [
      {
        "rule": "基本資料",
        "keywords": ["age", "health_status", "smoking"],
        "required": true,
        "class": "基本資料",
        "description": "年齡、健康狀況、吸菸習慣等基本資訊"
      },
      {
        "rule": "財力狀況",
        "keywords": ["property_proof"],
        "required": true,
        "class": "財力狀況",
        "description": "財力越佳，核保額度可放寬"
      },
      {
        "rule": "信用評價",
        "keywords": [
          "credit_rating",
          "credit_alert.credit_card_overdue_count",
          "credit_alert.bad_debt",
          "credit_alert.joint_credit_warning",
          "credit_alert.over_insurance",
          "credit_alert.duplicate_insurance",
          "credit_alert.abnormal_insurance"
        ],
        "required": true,
        "class": "信用評價",
        "description": "信用狀況與過往投保異常紀錄"
      },
      {
        "rule": "理賠與保單紀錄",
        "keywords": [
          "claim_records.claim_count",
          "claim_records.total_claim_amount",
          "claim_records.disputed",
          "insurance_history.status",
          "insurance_history.cancel_reason"
        ],
        "required": false,
        "class": "理賠與保單紀錄",
        "description": "理賠次數、金額、爭議情形、退保紀錄與原因"
      },
      {
        "rule": "人工審查",
        "keywords": [
          "review_records.manual_reviewed",
          "review_records.rejected",
          "review_records.pending"
        ],
        "required": false,
        "class": "人工審查",
        "description": "是否曾被人工審查、拒保或暫緩"
      },
      {
        "rule": "風險控管",
        "keywords": ["criminal_record.has_record", "criminal_record.blacklist"],
        "required": true,
        "class": "風險控管",
        "description": "有無犯罪前科與是否列入黑名單"
      },
      {
        "rule": "法遵管理",
        "keywords": [
          "suspicious_transaction.money_laundering",
          "suspicious_transaction.terrorist_financing"
        ],
        "required": true,
        "class": "法遵管理",
        "description": "有無疑似洗錢或恐怖融資紀錄"
      }
    ]
  }
}

"""