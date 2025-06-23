tomato_classes = [
    'Bacterial Spot', 'Early Blight', 'Late Blight', 'Leaf Mold',
    'Septoria Leaf Spot', 'Spider Mites', 'Target Spot',
    'Yellow Leaf Curl Virus', 'Mosaic Virus', 'Healthy'
]

treatments = {
    'Bacterial Spot': {
        'description': 'Bacterial disease causing small, water-soaked spots.',
        'organic': {
            'treatment': 'Remove infected leaves, apply copper sprays.',
            'instructions': 'Apply copper soap weekly.',
            'products': [{'name': 'Garden Safe Copper Soap', 'price': '$10.99', 'type': 'Organic'}]
        },
        'chemical': {
            'treatment': 'Use bactericides like streptomycin.',
            'instructions': 'Apply every 7–10 days.',
            'products': [{'name': 'Bonide Copper Fungicide', 'price': '$16.99', 'type': 'Chemical'}]
        }
    },
    'Early Blight': {
        'description': 'Fungal disease with dark brown spots and concentric rings.',
        'organic': {
            'treatment': 'Apply neem oil, remove debris.',
            'instructions': 'Spray neem oil every 7–14 days.',
            'products': [{'name': 'Bonide Neem Oil', 'price': '$11.98', 'type': 'Organic'}]
        },
        'chemical': {
            'treatment': 'Apply chlorothalonil or copper-based fungicides.',
            'instructions': 'Spray every 7–10 days.',
            'products': [{'name': 'Spectracide Immunox', 'price': '$12.97', 'type': 'Chemical'}]
        }
    },
    'Healthy': {
        'description': 'The plant appears healthy.',
        'organic': {
            'treatment': 'Use compost tea monthly.',
            'instructions': 'Maintain hygiene & monitor plant.',
            'products': [{'name': 'Dr. Earth Compost Tea', 'price': '$12.99', 'type': 'Organic'}]
        },
        'chemical': {
            'treatment': 'Preventive fungicides if needed.',
            'instructions': 'Spray every 14 days if required.',
            'products': [{'name': 'Spectracide Immunox', 'price': '$12.97', 'type': 'Chemical'}]
        }
    }
}

