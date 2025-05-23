# UniHousing - Student Housing Platform

UniHousing is a specialized digital platform connecting students with housing options in Monterrey, Mexico. The platform addresses critical market challenges by helping students find suitable accommodations near their universities and enabling property owners to market directly to their target student audience.

## 🚀 Current Features

### For Students
- **Property Search & Discovery**: Browse verified properties with university proximity data
- **Interactive Maps**: Mapbox-powered property visualization with distance calculations
- **Roommate Matching**: Find compatible roommates based on lifestyle preferences
- **Messaging System**: Direct communication with property owners
- **Viewing Requests**: Schedule property viewings with owners
- **University Integration**: Filter properties by proximity to specific universities

### For Property Owners
- **Property Management Dashboard**: Comprehensive dashboard for managing listings
- **Multi-Image Upload**: Upload and manage property photos with automatic optimization
- **Property Status Control**: Activate/deactivate listings with real-time visibility control
- **Tenant Communication**: Built-in messaging system for inquiries and viewings
- **Analytics & Insights**: Track property performance and viewing requests
- **Verification System**: Property and owner verification for trust building

### Technical Features
- **Bilingual Support**: Full English/Spanish internationalization
- **Responsive Design**: Mobile-first approach with cross-device compatibility
- **Real-time Updates**: Live status updates and notifications
- **Advanced Search**: Filter by price, location, amenities, and university proximity
- **Secure Authentication**: JWT-based authentication with automatic token refresh

## 🛠 Technology Stack

### Frontend
- **Framework**: Next.js 15 with App Router
- **Language**: TypeScript
- **Styling**: Tailwind CSS v4
- **Maps**: Mapbox GL JS
- **State Management**: React Context + hooks
- **HTTP Client**: Axios with automatic case conversion
- **Image Handling**: Next.js Image optimization + custom PropertyImage component

### Backend
- **Framework**: Django 5.2.1 + Django REST Framework
- **Database**: PostgreSQL with spatial extensions
- **Authentication**: Django SimpleJWT
- **File Storage**: Local storage (configurable for cloud)
- **API Documentation**: Auto-generated via DRF

### Development Tools
- **Containerization**: Docker & Docker Compose
- **Code Quality**: ESLint + TypeScript strict mode
- **Version Control**: Git with conventional commits

## 🚀 Getting Started

### Prerequisites
- **Docker & Docker Compose** (recommended)
- **Node.js 18+** (for local development)
- **Python 3.11+** (for local development)
- **PostgreSQL 15+** (for local development)

### Quick Start with Docker

1. **Clone the repository**
   ```bash
   git clone <your-repository-url>
   cd unihousing
   ```

2. **Environment Setup**
   ```bash
   # Frontend environment
   cp frontend/.env.example frontend/.env.local
   
   # Backend environment
   cp backend/.env.example backend/.env
   ```

3. **Configure Environment Variables**
   
   **Frontend (`frontend/.env.local`):**
   ```env
   NEXT_PUBLIC_API_URL=http://localhost:8000/api
   NEXT_PUBLIC_MAPBOX_ACCESS_TOKEN=your_mapbox_token_here
   ```
   
   **Backend (`backend/.env`):**
   ```env
   SECRET_KEY=your-secret-key-here
   DEBUG=True
   DATABASE_URL=postgres://postgres:postgres@db:5432/unihousing
   ALLOWED_HOSTS=localhost,127.0.0.1,backend
   ```

4. **Start the Application**
   ```bash
   docker-compose up --build
   ```

5. **Access the Application**
   - **Frontend**: http://localhost:3000
   - **Backend API**: http://localhost:8000/api
   - **Admin Interface**: http://localhost:8000/admin

### Local Development Setup

#### Backend Setup

1. **Create Virtual Environment**
   ```bash
   cd backend
   python -m venv venv
   source venv/bin/activate  # Windows: venv\Scripts\activate
   ```

2. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Database Setup**
   ```bash
   python manage.py migrate
   python manage.py createsuperuser
   ```

4. **Load Sample Data** (Optional)
   ```bash
   python manage.py loaddata universities/fixtures/initial_universities.json
   ```

5. **Start Development Server**
   ```bash
   python manage.py runserver
   ```

#### Frontend Setup

1. **Install Dependencies**
   ```bash
   cd frontend
   npm install
   ```

2. **Start Development Server**
   ```bash
   npm run dev
   ```

## 📁 Project Structure

### Backend

```
backend/
├── accounts/              # User authentication and profiles
├── properties/            # Property listings and management
├── universities/          # University data and proximity calculations
├── roommates/             # Roommate matching and profiles
├── messaging/             # User-to-user messaging system
└── unihousing_backend/    # Core Django settings and configuration
```

### Frontend

```
frontend/
├── public/                # Static assets
└── src/
    ├── app/
    │   ├── (auth)/        # Authentication routes (login, signup)
    │   ├── (dashboard)/   # Property owner dashboard
    │   └── (main)/        # Public routes (properties, universities)
    ├── components/        # Reusable React components
    ├── contexts/          # React context providers (auth, etc.)
    ├── lib/               # API services and utilities
    ├── types/             # TypeScript type definitions
    └── utils/             # Helper functions and utilities
```

### Key Files and Directories

#### Backend Key Files
- `accounts/models.py` - Custom User model with student/owner roles
- `properties/models.py` - Property, PropertyImage, Room models
- `properties/views.py` - Property CRUD operations and dashboard APIs
- `universities/models.py` - University data and proximity calculations
- `messaging/models.py` - Chat and viewing request system

#### Frontend Key Files
- `src/lib/api.ts` - API service with automatic case conversion
- `src/contexts/AuthContext.tsx` - User authentication state management
- `src/components/common/PropertyImage.tsx` - Optimized image component
- `src/app/(dashboard)/dashboard/` - Property owner management interface
- `src/types/api.ts` - TypeScript interfaces for API data

## 🔧 Development Workflow

### Adding New Features

1. **Backend Development**
   ```bash
   # Create new Django app
   cd backend
   python manage.py startapp new_feature
   
   # Add to INSTALLED_APPS in settings.py
   # Create models, serializers, views
   # Register URLs
   # Run migrations
   python manage.py makemigrations
   python manage.py migrate
   ```

2. **Frontend Development**
   ```bash
   # Create components in appropriate directories
   # Add API endpoints to lib/api.ts
   # Update TypeScript types in types/api.ts
   # Implement UI components with Tailwind CSS
   ```

### Key Development Notes

- **Case Conversion**: API automatically converts between snake_case (backend) and camelCase (frontend)
- **Authentication**: All protected routes require JWT token in Authorization header
- **Image Handling**: Use the `PropertyImage` component for consistent image display
- **Routing**: Follow the established (auth), (dashboard), (main) route group pattern

## 🗄 Database Models

### Core Models
- **User**: Extended authentication with student/owner roles
- **Property**: Property listings with detailed specifications
- **University**: University information with location data
- **PropertyImage**: Multi-image support for properties
- **RoommateProfile**: Student preferences for roommate matching
- **Conversation/Message**: Messaging system between users
- **ViewingRequest**: Property viewing appointment system

## 🌐 API Endpoints

### Authentication
- `POST /api/accounts/token/` - Login
- `POST /api/accounts/register/` - User registration
- `GET /api/accounts/profile/` - User profile

### Properties
- `GET /api/properties/` - List active properties
- `POST /api/properties/` - Create property (owners only)
- `GET /api/properties/{id}/` - Property details
- `PATCH /api/properties/{id}/toggle_active/` - Toggle property status
- `GET /api/properties/owner_properties/` - Owner's properties

### Universities
- `GET /api/universities/` - List universities

### Messaging
- `GET /api/messages/conversations/` - User conversations
- `POST /api/messages/conversations/start/` - Start conversation
- `POST /api/messages/viewings/` - Request property viewing

## 🚢 Deployment

### Production Build

1. **Build Frontend**
   ```bash
   cd frontend
   npm run build
   ```

2. **Collect Static Files**
   ```bash
   cd backend
   python manage.py collectstatic
   ```

3. **Production Docker**
   ```bash
   docker-compose -f docker-compose.prod.yml up -d
   ```

## 🧪 Testing

```bash
# Backend tests
cd backend
python manage.py test

# Frontend tests (when implemented)
cd frontend
npm test
```

## 📝 Contributing

1. **Create Feature Branch**
   ```bash
   git checkout -b feature/your-feature-name
   ```

2. **Follow Code Standards**
   - Use TypeScript for frontend
   - Follow Django conventions for backend
   - Use camelCase for frontend, snake_case for backend
   - Write descriptive commit messages

3. **Submit Pull Request**
   ```bash
   git push origin feature/your-feature-name
   ```

## 🛣 Roadmap

### Phase 1: Core Platform (Completed)
- ✅ User authentication system 
- ✅ Property listing and management
- 🔄 Basic messaging system
- 🔄 University proximity data

### Phase 2: Enhanced Features (In Progress)
- ✅ Property owner dashboard
- ✅ Image upload system
- ✅ Property status management
- 🔄 Roommate matching algorithm
- 🔄 Advanced search filters

### Phase 3: Growth Features (Planned)
- 📋 Payment integration
- 📋 Reviews and ratings system
- 📋 Mobile app development
- 📋 Multi-city expansion
- 📋 Advanced analytics

## 🐛 Known Issues

- Image optimization can be slow for large files
- Map performance needs optimization for large property datasets
- Mobile experience needs refinement

## 📞 Support

For development questions or issues:
- Check existing GitHub issues
- Create new issue with detailed description
- Include steps to reproduce for bugs

## 📄 License

This project is proprietary. All rights reserved.

---

**Built with ❤️ for the student community in Monterrey, Mexico**