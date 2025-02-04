Google sign in with OAuth
- Package to handle sign-in: `npm install @react-oauth/google@latest`
- Package to decode json web token: `npm install jwt-decode`


Main Configuration
```
import { StrictMode } from 'react'

import { createRoot } from 'react-dom/client'

import './index.css'

import App from './App.jsx'

import {GoogleOAuthProvider} from '@react-oauth/google'

const CLIENT_ID = "910191399735-r09g6dvoegpumoosu5mgqt1f59idkg33.apps.googleusercontent.com"

  

createRoot(document.getElementById('root')).render(

	<StrictMode>

		<GoogleOAuthProvider clientId={CLIENT_ID}>

			<App/>

		</GoogleOAuthProvider>

	</StrictMode>,

)
```
