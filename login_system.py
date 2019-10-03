{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Login System\n",
    "\n",
    "Creating a basic login system which will ask for username and password and will match it up with the one's existing in the database.\n",
    "\n",
    "STEP-1"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Username: admin\n",
      "Password: ········\n",
      "Incorrect password\n"
     ]
    }
   ],
   "source": [
    "import getpass\n",
    "# Setting a default username and password\n",
    "username=\"admin\"\n",
    "password=\"thenewdogwillbite\"\n",
    "\n",
    "# Taking the input of username\n",
    "u=input(\"Username: \")\n",
    "\n",
    "if u==username:\n",
    "    \n",
    "# Taking password as input\n",
    "    p=getpass.getpass('Password: ')\n",
    "    if p==password:\n",
    "        print(\"Logged in sucessfully!\")\n",
    "    else:\n",
    "        print(\"Incorrect password\")\n",
    "    \n",
    "else:\n",
    "    print('Invalid Username')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.6.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
