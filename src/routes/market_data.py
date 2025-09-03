from flask import Blueprint, jsonify
import requests
import random
from datetime import datetime, timedelta

market_data_bp = Blueprint('market_data', __name__)

# بيانات وهمية للأسواق العربية (في التطبيق الحقيقي ستأتي من APIs خارجية)
ARAB_MARKETS = {
    'saudi': {
        'name': 'السوق السعودي (تاسي)',
        'name_en': 'Saudi Stock Exchange (Tadawul)',
        'symbol': 'TASI',
        'base_value': 12000,
        'currency': 'SAR'
    },
    'dubai': {
        'name': 'سوق دبي المالي',
        'name_en': 'Dubai Financial Market',
        'symbol': 'DFM',
        'base_value': 3400,
        'currency': 'AED'
    },
    'egypt': {
        'name': 'بورصة مصر',
        'name_en': 'Egyptian Exchange',
        'symbol': 'EGX30',
        'base_value': 1200,
        'currency': 'EGP'
    },
    'kuwait': {
        'name': 'سوق الكويت',
        'name_en': 'Kuwait Stock Exchange',
        'symbol': 'KSE',
        'base_value': 7800,
        'currency': 'KWD'
    }
}

CRYPTO_DATA = {
    'bitcoin': {
        'name': 'بيتكوين',
        'name_en': 'Bitcoin',
        'symbol': 'BTC',
        'base_value': 67000
    },
    'ethereum': {
        'name': 'إيثريوم',
        'name_en': 'Ethereum',
        'symbol': 'ETH',
        'base_value': 3400
    },
    'ripple': {
        'name': 'ريبل',
        'name_en': 'Ripple',
        'symbol': 'XRP',
        'base_value': 0.67
    }
}

def generate_market_data(base_value, volatility=0.05):
    """توليد بيانات السوق مع تقلبات واقعية"""
    change_percent = random.uniform(-volatility, volatility)
    current_value = base_value * (1 + change_percent)
    change_value = current_value - base_value
    
    return {
        'current_value': round(current_value, 2),
        'change_value': round(change_value, 2),
        'change_percent': round(change_percent * 100, 2),
        'is_positive': change_percent >= 0,
        'last_updated': datetime.now().isoformat()
    }

@market_data_bp.route('/markets/arab', methods=['GET'])
def get_arab_markets():
    """الحصول على بيانات الأسواق العربية"""
    try:
        markets_data = {}
        
        for market_id, market_info in ARAB_MARKETS.items():
            market_data = generate_market_data(market_info['base_value'])
            markets_data[market_id] = {
                **market_info,
                **market_data
            }
        
        return jsonify({
            'success': True,
            'data': markets_data,
            'timestamp': datetime.now().isoformat()
        })
    
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

@market_data_bp.route('/markets/crypto', methods=['GET'])
def get_crypto_data():
    """الحصول على بيانات العملات المشفرة"""
    try:
        crypto_data = {}
        
        for crypto_id, crypto_info in CRYPTO_DATA.items():
            market_data = generate_market_data(crypto_info['base_value'], volatility=0.08)
            crypto_data[crypto_id] = {
                **crypto_info,
                **market_data,
                'currency': 'USD'
            }
        
        return jsonify({
            'success': True,
            'data': crypto_data,
            'timestamp': datetime.now().isoformat()
        })
    
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

@market_data_bp.route('/news/financial', methods=['GET'])
def get_financial_news():
    """الحصول على الأخبار المالية"""
    try:
        # أخبار وهمية (في التطبيق الحقيقي ستأتي من مصادر إخبارية)
        news_data = [
            {
                'id': 1,
                'title': 'البنك المركزي السعودي يرفع أسعار الفائدة بـ 0.25%',
                'summary': 'قرر البنك المركزي السعودي رفع أسعار الفائدة استجابة للتضخم العالمي',
                'source': 'العربية',
                'published_at': (datetime.now() - timedelta(hours=2)).isoformat(),
                'category': 'monetary_policy',
                'importance': 'high'
            },
            {
                'id': 2,
                'title': 'أرامكو تعلن عن أرباح قياسية للربع الثالث',
                'summary': 'حققت شركة أرامكو السعودية أرباحاً صافية بلغت 32.6 مليار دولار',
                'source': 'رويترز',
                'published_at': (datetime.now() - timedelta(hours=4)).isoformat(),
                'category': 'earnings',
                'importance': 'high'
            },
            {
                'id': 3,
                'title': 'صندوق الاستثمارات العامة يستثمر في التكنولوجيا المالية',
                'summary': 'أعلن الصندوق عن استثمارات جديدة في قطاع التكنولوجيا المالية بقيمة 5 مليارات دولار',
                'source': 'الاقتصادية',
                'published_at': (datetime.now() - timedelta(hours=6)).isoformat(),
                'category': 'investment',
                'importance': 'medium'
            },
            {
                'id': 4,
                'title': 'ارتفاع أسعار النفط إلى أعلى مستوى في 3 أشهر',
                'summary': 'وصلت أسعار النفط الخام إلى 85 دولاراً للبرميل وسط توقعات بزيادة الطلب',
                'source': 'بلومبرغ',
                'published_at': (datetime.now() - timedelta(hours=8)).isoformat(),
                'category': 'commodities',
                'importance': 'medium'
            },
            {
                'id': 5,
                'title': 'البنك المركزي الإماراتي يطلق عملة رقمية تجريبية',
                'summary': 'بدء تجربة العملة الرقمية للبنك المركزي في إطار مشروع رقمنة النظام المصرفي',
                'source': 'الخليج',
                'published_at': (datetime.now() - timedelta(hours=10)).isoformat(),
                'category': 'digital_currency',
                'importance': 'medium'
            }
        ]
        
        return jsonify({
            'success': True,
            'data': news_data,
            'total_count': len(news_data),
            'timestamp': datetime.now().isoformat()
        })
    
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

@market_data_bp.route('/economic-calendar', methods=['GET'])
def get_economic_calendar():
    """الحصول على التقويم الاقتصادي"""
    try:
        # أحداث اقتصادية وهمية
        calendar_events = [
            {
                'id': 1,
                'title': 'اجتماع البنك المركزي السعودي',
                'description': 'اجتماع لجنة السياسة النقدية لمناقشة أسعار الفائدة',
                'date': (datetime.now() + timedelta(days=2)).isoformat(),
                'time': '14:00',
                'country': 'السعودية',
                'country_code': 'SA',
                'importance': 'high',
                'category': 'monetary_policy',
                'previous': None,
                'forecast': None,
                'actual': None
            },
            {
                'id': 2,
                'title': 'بيانات التضخم الإماراتية',
                'description': 'نشر بيانات مؤشر أسعار المستهلك للشهر الماضي',
                'date': (datetime.now() + timedelta(days=1)).isoformat(),
                'time': '10:00',
                'country': 'الإمارات',
                'country_code': 'AE',
                'importance': 'medium',
                'category': 'inflation',
                'previous': '2.1%',
                'forecast': '2.3%',
                'actual': None
            },
            {
                'id': 3,
                'title': 'بيانات الناتج المحلي الإجمالي المصري',
                'description': 'نشر بيانات النمو الاقتصادي للربع الثالث',
                'date': (datetime.now() + timedelta(days=3)).isoformat(),
                'time': '12:00',
                'country': 'مصر',
                'country_code': 'EG',
                'importance': 'high',
                'category': 'gdp',
                'previous': '4.2%',
                'forecast': '4.5%',
                'actual': None
            }
        ]
        
        return jsonify({
            'success': True,
            'data': calendar_events,
            'total_count': len(calendar_events),
            'timestamp': datetime.now().isoformat()
        })
    
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

@market_data_bp.route('/analysis/technical', methods=['GET'])
def get_technical_analysis():
    """الحصول على التحليلات الفنية"""
    try:
        technical_analysis = [
            {
                'id': 1,
                'title': 'تحليل فني للسوق السعودي - نظرة أسبوعية',
                'summary': 'يظهر المؤشر العام للسوق السعودي إشارات إيجابية مع كسر مستوى المقاومة عند 12,300 نقطة',
                'market': 'saudi',
                'timeframe': 'weekly',
                'trend': 'bullish',
                'support_levels': [12000, 11800, 11600],
                'resistance_levels': [12500, 12700, 13000],
                'indicators': {
                    'rsi': 65.4,
                    'macd': 'positive',
                    'moving_average_50': 12150,
                    'moving_average_200': 11900
                },
                'recommendation': 'شراء',
                'confidence': 75,
                'author': 'فريق التحليل الفني',
                'published_at': (datetime.now() - timedelta(hours=1)).isoformat()
            },
            {
                'id': 2,
                'title': 'تحليل البيتكوين - اختبار مستوى الدعم الحرج',
                'summary': 'يختبر البيتكوين مستوى دعم مهم عند 65,000 دولار مع توقعات بارتداد قوي',
                'market': 'bitcoin',
                'timeframe': 'daily',
                'trend': 'neutral',
                'support_levels': [65000, 62000, 58000],
                'resistance_levels': [70000, 73000, 75000],
                'indicators': {
                    'rsi': 45.2,
                    'macd': 'negative',
                    'moving_average_50': 66500,
                    'moving_average_200': 64000
                },
                'recommendation': 'انتظار',
                'confidence': 60,
                'author': 'محلل العملات المشفرة',
                'published_at': (datetime.now() - timedelta(hours=3)).isoformat()
            }
        ]
        
        return jsonify({
            'success': True,
            'data': technical_analysis,
            'total_count': len(technical_analysis),
            'timestamp': datetime.now().isoformat()
        })
    
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

